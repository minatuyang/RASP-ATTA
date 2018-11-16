import RPi.GPIO as GPIO
import time
import signal
import atexit


class ServoControl(object):
    def __init__(self, maxAngle=180.0, minAngle=0.0, gpio=None):
        self.angle = None
        self._gpio = gpio
        self._freq = 50
        self._maxAngle = maxAngle
        self._minAngle = minAngle
        self.p = None
        if self._maxAngle > 180.0 or self._maxAngle < 0.0:
            raise Exception("Invalid maxAngle", OverflowError)
        if self._minAngle > 180.0 or self._minAngle < 0.0:
            raise Exception("Invalid minAngle", OverflowError)
        if self._minAngle > self._maxAngle:
            raise Exception(
                "Invalid maxAngle: minAngle > maxAngle", OverflowError)

    @property
    def gpio(self):
        return self._gpio

    @gpio.setter
    def gpio(self, value):
        if self._gpio != value:
            self._gpio = value

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        if self._freq != value:
            self._freq = value

    @property
    def maxAngle(self):
        return self._maxAngle

    @maxAngle.setter
    def maxAngle(self, value):
        if (value > 180 or value < 0) or value < self._minAngle:
            raise Exception("Invalid number!", OverflowError)
        if self._maxAngle != value:
            self._maxAngle = value

    @property
    def minAngle(self):
        return self._minAngle

    @minAngle.setter
    def minAngle(self, value):
        if (value > 180 or value < 0) or value > self._maxAngle:
            raise Exception("Invalid number!", OverflowError)
        if self._minAngle != value:
            self._minAngle = value

    def changeAngle(self, value):
        if value < self._minAngle:
            angle = _minAngle
        if value > self._maxAngle:
            angle = _maxAngle
        if self.angle != value:
            self.angle = value
        cycle = 2.5+(1/18.0)*self.angle
        self.p.ChangeDutyCycle(cycle)
        time.sleep(0.2)
        self.p.ChangeDutyCycle(0)

    def start(self):
        if self._gpio is None:
            raise Exception("Invalid number!", OverflowError)
            pass
        GPIO.setup(self._gpio, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self._gpio, self._freq)
        self.p.start(0)


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.cleanup
    atexit.register(GPIO.cleanup)  # 在程序退出时执行GPIO指令清空
    GPIO.setmode(GPIO.BCM)  # 设置GPIO的编号格式为BCM
    # BCM/BOARD
    # 可以在树莓派终端中输入gpio readall来查询GPIO的BCM编号
    servo1 = ServoControl(gpio=15)
    servo1.start()
    servo2 = ServoControl(gpio=18)
    servo2.start()
    time.sleep(1)

    while True:
        servo1.changeAngle(90)
        servo2.changeAngle(90)
        time.sleep(2)
        servo1.changeAngle(0)
        servo2.changeAngle(0)
        time.sleep(2)
