import cv2

webcamera = cv2.VideoCapture(0)

while True:
    camera, frame = webcamera.read()
    
    cv2.imshow('Imagem WebCam', frame)
    
    if cv2.waitKey(1) == ord('q'): 
        break
    
webcamera.release()
cv2.destroyAllWindows()
