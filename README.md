# zoro_rqt_reconfigure
    使用zoro_rqt_reconfigure需要安装PyQt5和PySide2，即
```
sudo pip3 install PyQt5==5.10
sudo pip3 install PySide2==5.11.2
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

 2、如果要运行在本地机器的docker里面，需要进行下列配置：
 ```
 在docker启动的时候加入 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY 
 同时在本机上执行 xhost +
 ```

 3、如果要运行在远程机器的docker里面，需要进行下列配置：
 在本机上：
 ```
 sudo vim /etc/lightdm/lightdm.conf
 在文件中加入下列两行
 [SeatDefaults]
 xserver-allow-tcp=true

 然后重启 sudo systemctl restart lightdm
 xhost +
 ```

 在docker上：
 ```
 启动docker时加入 -e DISPLAY=本机ip:0.0
 或者进入docker  export DISPLAY=本机ip:0.0
 ```
