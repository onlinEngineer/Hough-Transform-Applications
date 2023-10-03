import cv2 as cv
import numpy as np


cap = cv.VideoCapture('input/test_video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    fps=cap.get(cv.CAP_PROP_FPS)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray, 50, 200, None, 3)

    linesP = cv.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(frame, (l[0], l[1]), (l[2], l[3]), (0,0,255), 2, cv.LINE_AA)

    cv.putText(frame, str(fps), (7, 70), cv.FONT_HERSHEY_PLAIN,3, (100, 255, 0), 3, cv.LINE_AA)
    

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()