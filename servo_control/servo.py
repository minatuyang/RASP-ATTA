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
        if self._maxAngle > 180.0 or self._maxAngle < 0.0:
            raise Exception("Invalid maxAngle", OverflowError)
            pass
        if self._minAngle > 180.0 or self._minAngle < 0.0:
            raise Exception("Invalid minAngle", OverflowError)
            pass
        if self._minAngle > self._maxAngle:
            raise Exception(
                "Invalid angle: minAngle > maxAngle", OverflowError)
            pass

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

    @gfreq.setter
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
        if (value > 180 or value < 0):
            raise Exception("Invalid number!", OverflowError)
            pass
        if value < self._minAngle or value > self._maxAngle:
            pass  # angle=minAngle or angle= maxAngle
            raise Exception("Invalid number!", OverflowError)
            pass
        if self.angle != value:
            self.angle = value
        cycle = 2.5+(1/18.0)*self.angle
        self.p.ChangeDutyCycle(cycle)

    def start(self):
        if self._gpio is None:
            raise Exception("Invalid number!", OverflowError)
            pass
        GPIO.setup(self._gpio, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self._gpio, self._freq)
        self.p.start(0)


if __name__ == "__main__":
    atexit.register(GPIO.cleanup)
    GPIO.cleanup
    GPIO.setmode(GPIO.BCM)
    # servo1 = ServoControl(minAngle=17.0, maxAngle=167.0)
    # print(servo1.minAngle)
    # print(servo1.maxAngle)
    # print(servo1.angle)
    # servo1.minAngle = 20
    # servo1.maxAngle = 170
    # print(servo1.maxAngle)
    # servo1.changeAngle(140.0)
    # print(servo1.angle)
    servo1 = ServoControl(gpio=15)
    servo1.start()
    servo2 = ServoControl(gpio=18)
    servo2.start()
    while True:
        servo1.changeAngle(90)
        servo2.changeAngle(90)
        time.sleep(1)
        servo1.changeAngle(0)
        servo2.changeAngle(0)
