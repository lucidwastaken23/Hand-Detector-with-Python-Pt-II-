import cv2
import mediapipe as mp
import time
import Handdetectormodule as htm

pTime = 0
cTime = 0

wCam,hCam = 640, 488
cap = cv2.VideoCapture(0)  #type 1 for usb connected webcam
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detecrtionCon = 0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw = False)
    if len(lmlist) != 0:
        print(lmlist[4])
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10,70), cv2.FONT_HERSHEY_COMPLEX,
                3, (255,0,255), 3)


    cv2.imshow("Frame", img)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()