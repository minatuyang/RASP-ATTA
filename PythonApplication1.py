import time
import cv2
import numpy as np


class CaptureManager(object):
    def __init__(self, capture, previewWindowManager=None, shouldMirrorPreview=False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None


cameraCapture = cv2.VideoCapture(0)
ret = True
while ret:
    ret, frame = cameraCapture.read()
    # frame=cv2.flip(frame,0)#上下翻转
    frame = cv2.flip(frame, 1)  # 左右翻转
    cv2.imshow('My Camera', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cameraCapture.release()
a = bin
cv2.destroyAllWindows()
