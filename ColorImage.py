import numpy as np
import cv2

class ColorImage:

    def __init__(self, ruta_imagen):
        self.ruta_imagen = ruta_imagen #Guarda la ruta de la imagen en la variable ruta_imagen.
        self.image=cv2.imread(self.ruta_imagen) #Lee la imagen según la ruta correspondiente y la guarda en la variable image.
        self.imageRGB= np.copy(self.image) #Realiza una copia de la imagen.

    def DisplayProperties(self):
        self.DisplayProperties=self.image.shape #Guarda las dimensiones de la imagen, tales como altura, ancho y canales.
        print(self.DisplayProperties)  #Muestra en pantalla las dimensiones de la imagen.

    def MakeGray(self):
        self.MakeGray=cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #Convierte la imagen a una versión de grises.
        cv2.imshow('GrayImage', self.MakeGray)#Muestra la imagen gris en la pantalla.
        cv2.waitKey(0)

    def ColorizeRGB(self, color_deseado):
        self.color_deseado=color_deseado

        if color_deseado == 'Red':
            RedImage = self.image #Guarda la imagen original en RedImage.
            RedImage[:, :, 0] = 0 #La componente blue de la imagen se iguala a 0.
            RedImage[:, :, 1] = 0 #La componente green de la imagen se iguala a 0.
            RedImage[:, :, 2] = self.MakeGray #La componente roja se iguala a la imagen en tonos grises.
            cv2.imshow('RedImage', RedImage) #Muestra la imagen rojiza en la pantalla.
            cv2.waitKey(0)

        if color_deseado == 'Green':
            GreenImage = self.image #Guarda la imagen original en GreenImage.
            GreenImage[:, :, 0] = 0 #La componente blue de la imagen se iguala a 0.
            GreenImage[:, :, 2] = 0 #La componente red de la imagen se iguala a 0.
            GreenImage[:, :, 1] = self.MakeGray #La componente green se iguala a la imagen en tonos grises.
            cv2.imshow('GreenImage', GreenImage) #Muestra la imagen verdoza en la pantalla.
            cv2.waitKey(0)

        if color_deseado == 'Blue':
            BlueImage = self.image #Guarda la imagen original en Blue Image.
            BlueImage[:, :, 1] = 0 #La componente green de la imagen se iguala a 0.
            BlueImage[:, :, 2] = 0 #La componente red de la imagen se iguala a 0.
            BlueImage[:, :, 0] = self.MakeGray #La componente blue se iguala a la imagen en tonos grises.
            cv2.imshow('BlueImage', BlueImage) #Muestra la imagen azuloza en la pantalla.
            cv2.waitKey(0)

    def MakeHue(self):
        self.MakeHue1=cv2.cvtColor(self.imageRGB, cv2.COLOR_BGR2HSV) #Convierte la imagen original a HSV.
        self.MakeHue1[:, :, 1] = 255 #La componente S se iguala a 255.
        self.MakeHue1[:, :, 2] = 255 #La componente V se iguala a 255.
        self.MakeHue=cv2.cvtColor(self.MakeHue1, cv2.COLOR_HSV2BGR) #Convierte la imagen HSV a RGB.
        cv2.imshow('HSVImage', self.MakeHue) #Muestra la imagen RGB en la pantalla.
        cv2.waitKey(0)
