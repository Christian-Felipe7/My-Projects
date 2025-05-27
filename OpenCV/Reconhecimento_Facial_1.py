import cv2

carregaAlgoritmo = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('images/imagem2.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=3)

# padrão em scalefactor é 1.1
# scaleFactor=x, minNeighbors=x, minSize=(30, 30) -> padrão
print(faces)

for (x, y, w, l) in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + l), (0, 255, 0), 2)

cv2.imshow('Faces', imagem)
cv2.waitKey()
