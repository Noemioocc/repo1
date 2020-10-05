import cv2
import numpy as np

imagen = cv2.imread(r'/home/noemi/Escritorio/Blog_Betico/IMG_1674.JPG',1)
newImg = cv2.resize(imagen, (250, 250))
cv2.imshow('Resized Image', newImg)
cv2.imwrite("/home/noemi/Escritorio/Blog_Betico/imagenesOK/imagen1.jpg",newImg)

