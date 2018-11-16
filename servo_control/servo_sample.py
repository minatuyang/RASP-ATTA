import RPi.GPIO as GPIO
import time
import signal
import atexit
import numpy as np
atexit.register(GPIO.cleanup)  # 在程序退出时执行GPIO指令清空
GPIO.setmode(GPIO.BCM)  # 设置GPIO的编号格式为BCM
# BCM/BOARD
# 可以在树莓派终端中输入gpio readall来查询GPIO的BCM编号

GPIO.setup(15, GPIO.OUT, initial=False)  # 设置GPIO为推挽模式
GPIO.setup(18, GPIO.OUT, initial=False)
p1 = GPIO.PWM(15, 50)  # 设置GPIO为50Hz的PWM输出
p2 = GPIO.PWM(15, 50)  # 50HZ

p1.start(0)  # 开始PWM输出，输出占空比为0
p2.start(0)

time.sleep(2)

while True:
    p.ChangeDutyCycle(12.5)  # 设置转动角度至180
    time.sleep(0.2)
    p.ChangeDutyCycle(0)  # 保持当前角度
    time.sleep(5)

    p.ChangeDutyCycle(2.5)  # 设置转动角度至0
    time.sleep(0.2)
    p.ChangeDutyCycle(0)  # 保持当前角度
    time.sleep(5)
