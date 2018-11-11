import cv2
camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    if not ret:
        break
    #frame = cv2.flip(frame, 0)  # 上下翻转
    frame = cv2.flip(frame, 1)  # 左右翻转
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow('source', frame)
    cv2.imshow('frame', gray)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
camera.release()
cv2.destroyAllWindows()
