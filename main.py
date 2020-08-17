from ColorImage import *
import cv2


if __name__=='__main__':
    ruta_imagen = input('Introduzca la ruta del archivo: ') #Pide al usuario la ruta del archivo.
    imagen= ColorImage(ruta_imagen) #Crea la imagen con el fin de utilizar la clase.
    imagen.DisplayProperties() #Hace llamado a la función DisplayProperties de la clase ColorImage.
    imagen.MakeGray() #Hace llamado a la función MakeGray de la clase ColorImage.
    imagen.ColorizeRGB('Red') #Hace llamado a la función ColorizeRGB de la clase ColorImage y se introduce la opción Red.
    imagen.MakeHue() #Hace llamado a la función MakeHue de la clase ColorImage.

#C:/Users/ASUS-PC/Desktop/lena.png