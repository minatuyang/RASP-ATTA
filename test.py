import cv2
import numpy as np

clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


def mousemove(event, x, y, s, p):
    global frame, current_measurement, measurements, last_measurement, current_prediction, last_prediction
    last_prediction = current_prediction
    last_measurement = current_measurement
    current_measurement = np.array([[np.float32(x)], [np.float32(y)]])
    kalman.correct(current_measurement)
    current_prediction = kalman.predict()
    lmx, lmy = last_measurement[0], last_measurement[1]
    cmx, cmy = current_measurement[0], current_measurement[1]
    lpx, lpy = last_prediction[0], last_prediction[1]
    cpx, cpy = current_prediction[0], current_prediction[1]
    cv2.line(frame, (lmx, lmy), (cmx, cmy), (0, 100, 0))
    cv2.line(frame, (lpx, lpy), (cpx, cpy), (0, 0, 200))


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('test')
cv2.setMouseCallback('test', onMouse)
_, frame = cameraCapture.read()
while cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('test', frame)
    _, frame = cameraCapture.read()


class Pedestrian():
    def __init__(self, id, frame, track_window):
        self.id = int(id)
        x, y, w, h = track_window
        self.track_window = track_window
        self.roi = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2HSV)
        roi_hist = cv2.calcHist([self.roi], [0], None, [16], [0, 180])
        self.roi_hist = cv2.normalize(
            roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
        self.kalman = cv2.KalmanFilter(4, 2)
        self.kalman.measurementMatrix = np.array(
            [[1, 0, 1, 0], [0, 1, 0, 0]], np.float32)
        self.kalman.transitionMatrix = np.array(
            [[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
        self.kalman.processNoiseCov = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.03
        self.measurement = np.array((2, 1), np.float32)
        self.prediction = np.zeros((2, 1), np.float32)
        self.term_crit = (cv2.TermCriteria_EPS |
                          cv2.TERM_CRITERIA_COUNT, 10, 1)
        self.center = None
        self.update(frame)

    def __del__(self):
        print('aaa %d destroyed', self.id)

    def update(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        back_project = cv2.calcBackProject(
            [hsv], [0], self.roi_hist, [0, 180], 1)
        if args.get("algorithm") == "c":
            ret, self.track_window = cv2.Camshift(
                back_project, self.track_window, self.term_crit)
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            self.center = center(pts)
            cv2.polylines(frame, [pts], True, 255, 1)
        if not args.get("algorithm") or args.get("algorithm") == "m":
            ret, self.track_window = cv2.meanShift(
                back_project, self.track_window, self.term_crit)
            x, y, w, h = self.track_window
            self.center = center(
                [[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 1)
        self.kalman.correct(self.center)
        prediction = self.kalman.predict()
        cv2.circle(frame, (int(prediction[0]), int(
            prediction[1])), 4, (0, 255, 0), -1)
        # cv2.putText(frame,"ID")


cv2.destroyAllWindows()
cameraCapture.release()
