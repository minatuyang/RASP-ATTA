# 实现舵机控制的封装  
## 环境：  
### 硬件：  
> Raspberry Pi 3B+  
> SG 90
### 软件：
> RASPBIAN STRETCH WITH DESKTOP（Version:October 2018  Kernel version:4.14）  
> python 3.5  
> opencv 3.4.3  
## 背景知识（部分来源网络）：  
### SG 90舵机：  
> 这个舵机是模拟舵机，而非数字舵机，这两者的区别是这样，数字舵机只要给一个PWM信号即可，这个信号是目的地的位置，舵机会自动旋转到这个位置，而 模拟舵机需要一直给予目的地的PWM信号。由于舵机需要的PWM信号实际就是一个方波，所以模拟舵机就是需要不断的重复发一样的方波，直到舵机旋转到指定 的位置，并且如果需要锁定在这个位置，那么还需继续给予这个方波。  
> 舵机，是指在自动驾驶仪中操纵飞机舵面（操纵面）转动的一种执行部件。分有：  
> ①电动舵机，由电动机、传动部件和离合器组成。接受自动驾驶仪的指令信号而工作，当人工驾驶飞机时，由于离合器保持脱开而传动部件不发生作用。  
> ②液压舵机，由液压作动器和旁通活门组成。当人工驾驶飞机时，旁通活门打开，由于作动器活塞两边的液压互相连通而不妨害人工操纵。  
> 此外，还有电动液压舵机，简称“电液舵机”。  
> 舵机的大小由外舾装按照船级社的规范决定，选型时主要考虑扭矩大小。如何审慎地选择经济且合乎需求的舵机，也是一门不可轻忽的学问。  
> 0.5ms-------------0度；   2.5%   
> 1.0ms------------45度；   5.0%   
> 1.5ms------------90度；   7.5%  
> 2.0ms-----------135度；   10.0%  
> 2.5ms-----------180度；   12.5%  


## 参考代码（部分来源网络）：  
> ```C++   
> void main(void)  
> {  
>       DUOJI=1;  
>       Delay500us();    
>       Delay500us();    
>       DUOJI=0;    
>       Delay500us();  
>       Delay500us();  
>       while(1)  
>       {  
>           DUOJI=1;  
>           Delay500us();  
>           Delay500us();  
>           DUOJI=0;  
>           Delay500us();  
>           Delay500us();  
>       }  
> }    
## 参考文献：  
> [SG90 9g舵机单片机控制的一些注意事项](http://www.51hei.com/bbs/dpj-78449-1.html)     
> [Stanford AI Lab](http://ai.stanford.edu/)   
> [Stanford AI Lab——Jonathan Krause](http://ai.stanford.edu/~jkrause/)   
> [piwheels](https://www.piwheels.org/)    
> [树莓派自身摄像头的opencv调用](http://www.cnblogs.com/LaplaceAkuir/p/5271962.html)    
> [在OpenCV中调用CSI摄像头](https://blog.csdn.net/Deiki/article/details/71123947)   
> [参考文献](http://www.computervisionblog.com)     
## 训练集下载参考链接：  
> [Cognitive Computation Group](http://cogcomp.org/page/data/)     
[Stanford AI Lab——cardata——Jonathan Krause](http://ai.stanford.edu/~jkrause/cars/car_dataset.html)    


sudo apt-get install libcv-dev
