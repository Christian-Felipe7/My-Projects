import cv2

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('images/imagem5.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagemCinza)

for (x, y, w, l) in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + l), (0, 255, 0), 2)
    
cv2.imshow('faces', imagem)
cv2.waitKey()
