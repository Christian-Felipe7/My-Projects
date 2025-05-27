import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('images/imagem5.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza)

print(faces)

for (x, y, w, l) in faces:
    leitura = cv2.rectangle(imagem, (x, y), (x + w, y + l), (0, 255, 0), 2)
    localOlho = leitura[y:y + l, x:x + w]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = carregaOlho.detectMultiScale(localOlhoCinza, scaleFactor=1.3, minNeighbors=9)
    
    for(ox, oy, ow, ol) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ow, oy + ol), (255 , 0, 255), 2)
        
cv2.imshow('Detecta Face e os Olhos', imagem)
cv2.waitKey()
