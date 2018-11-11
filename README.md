# **RASP-ATTA**
---------------------------------------------------
## 项目简介  
Automatic target tracking algorithm based on raspberry-pi  
一个基于树莓派实现的云台自动跟踪模型  
## 环境基础   
### 树莓派简介     
> 树莓派是一个迷你电脑，集成在一块电路板。目前，最新的型号有两个。   
（1）Raspberry Pi 3代 B 型    
（2）Raspberry Pi zero （含 zero w）    
虽然后者便宜，但是少了许多接口（比如只有一个 USB 口），CPU 和内存都比较低，配件也少，因此推荐购买第3代的 B 型。以下都针对这个型号，但大部分内容对 zero 也适用。   
它是一款基于ARM的微型电脑主板，以SD/MicroSD卡为内存硬盘，卡片主板周围有1/2/4个USB接口和一个10/100 以太网接口（A型没有网口），可连接键盘、鼠标和网线，同时拥有视频模拟信号的电视输出接口和HDMI高清视频输出接口，以上部件全部整合在一张仅比信用卡稍大的主板上，具备所有PC的基本功能只需接通电视机和键盘，就能执行如电子表格、文字处理、玩游戏、播放高清视频等诸多功能。   
### Raspbian环境搭建
> sudo apt-get update  
sudo apt-get upgrade  
sudo rpi-update   
sudo passwd root  
sudo apt-get install libatlas-base-dev   
sudo apt-get install libgflags-dev  
sudo apt-get install libgoogle-glog-dev   
sudo apt-get install liblmdb-dev   
sudo apt-get install libgflags-dev  
sudo apt-get install python   
sudo apt-get install python-dev   
sudo apt-get install python-numpy   
sudo apt-get install ipython   
sudo apt-get install ipython-notebook   
sudo apt-get install python-sklearn   
sudo apt-get install python-skimage   
sudo apt-get install python-protobuf  
sudo apt-get install vim  
sudo apt-get install qt-sdk  
sudo apt-get install qt5-default  
sudo apt-get install qt4-default  
sudo apt-get install qtcreator  
sudo apt-get install libboost-all-dev  
sudo apt-get install gdebi   
sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev   libswscale-dev  
sudo apt-get install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev  
sudo apt-get install libprotobuf-dev libleveldb-dev   libsnappy-dev libhdf5-serial-dev protobuf-compiler   libatlas-base-dev  
sudo apt-get install libopencv-dev  
sudo pip3 install numpy scipy  
sudo pip3 install opencv-python  
sudo pip3 install opencv-contrib-python
sudo pip3 install autopep8 imutils    
>      
> sudo vim /etc/modules   
在文件中l2c-dev前面增加一行：bcm2835-v4l2（小写的L）这样就可以解决cvideocaptrue不能获取图像的问题了   

## 人脸检测算法  
## 舵机控制  
## 目标跟踪算法  
## 系统功能实现
