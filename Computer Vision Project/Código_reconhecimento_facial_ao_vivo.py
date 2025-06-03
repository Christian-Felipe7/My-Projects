import cv2

webCamera = cv2.VideoCapture(0)
classificarVideoFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    camera, frame = webCamera.read()
    
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificarVideoFace.detectMultiScale(cinza)
    
    for(x, y, w, l) in detecta:
        cv2.rectangle(frame, (x, y), (x + w, y + l), (0, 255, 0), 2)
        
    cv2.imshow('Video WebCam', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
webCamera.release()
cv2.destroyAllWindows()
