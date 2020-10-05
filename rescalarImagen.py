import cv2
import numpy as np
#Abrir una imagen desde una direccion
imagen = cv2.imread(r'/home/noemi/Escritorio/Blog_Betico/IMG_1674.JPG',1)
#rescalar la imagen 250 x 250
newImg = cv2.resize(imagen, (250, 250))
#cv2.imshow('Resized Image', newImg)
#Guadar la imagen redimensionada en una direccion especifica
cv2.imwrite("/home/noemi/Escritorio/Blog_Betico/imagenesOK/imagen1.jpg",newImg)

