import os
import dynamic_reconfigure._dynamic_reconfigure_ as dy

class client:
    def __init__(self, remote_name, timeout, config_callback=None):
        self.remote_name = remote_name
        self.timeout = timeout
        self.config_callback = config_callback

    def get_group_descriptions(self):
        description = dy.get_description(self.remote_name)
        names = []
        for k in description.keys():
            if (k[0:4] == 'name'):
                names.append(k[5:])
        dic = {'groups': {}, 'state': True, 'name': 'Default', 'parent': 0, 'type': '', 'id': 0}
        dic['parameters'] = []
        for name in names:
            parameter = {}
            parameter['edit_method'] = description['edit.' + name]
            parameter['name'] = name
            parameter['min'] = description['min.' + name]
            parameter['max'] = description['max.' + name]
            #parameter['value'] = description['value.' + name]
            parameter['level'] = description['lev.' + name]
            parameter['default'] = description['default.' + name]
            parameter['type'] = description['type.' + name]
            parameter['description'] = description['des.' + name]

            dic['parameters'].append(parameter)
        #print(dic)
        return dic

    def update_configuration(self, configs_tobe_updated):
        in_dict = {}
        for k in configs_tobe_updated.keys():
            in_dict['value.' + k] = configs_tobe_updated[k]
        values = dy.update_parameters(self.remote_name, in_dict)
        names = []
        for k in values.keys():
            if (k[0:5] == 'value'):
                names.append(k[6:])
                #print(k[0:4], k[5:])
        dic = {}
        for name in names:
            dic[name] = values['value.' + name]
        dic['groups'] = dic.copy()
        dic['groups']['groups'] = ''
        self.config_callback(dic)

    def close(self):
        return
    def update(self):
        return 1

def find_reconfigure_services():
    cmd = 'zoro node list -a | grep ^_DynamicReconfigure'
    ret = os.popen(cmd, 'r', 1).read().split()
    servers = []
    for s in ret:
        servers.append("/" + s)
    return servers


def DynamicReconfigureParameterException():
    return 0

def DynamicReconfigureCallbackException():
    return 0

