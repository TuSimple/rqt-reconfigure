# zoro_rqt_reconfigure
    使用zoro_rqt_reconfigure需要安装PyQt5，即
```
sudo pip3 install PyQt5
```

# 运行

    1，编译zoro_dynamic_reocnfigure,并source zoro_dynamic_reocnfigure_ws/install/local_setup.bash
    2，编译zoro_rqt_reconfigure,并source 编译zoro_rqt_reconfigure_ws/install/local_setup.bash
    3，通过运行script中的zoro_rqt_run， 即： ./zoro_rqt_reconfigure_ws/install/script/rqt_gui
    
# 注意
 1、如果出现如下错误：
 ```
 This application failed to start because it could not find or load the Qt platform plugin "xcb"
in "".

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, xcb.

Reinstalling the application may fix this problem.
已放弃 (核心已转储)
```
   可以输入：
```
export LD_LIBRARY_PATH=/usr/local/lib/python3.5/dist-packages/PyQt5/Qt/lib:$LD_LIBRARY_PATH
```
