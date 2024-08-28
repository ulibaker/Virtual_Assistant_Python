#Template de deteccion de camara

import cv2

#Usamos la libreria de opencv para usar la camara y procesar la informacion
#Y compararla con la que se tiene en el archivo xml
fade_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#Ciclo While que se utiliza para procesar las imagenes que obtiene la camara
#En caso de que detecte algun rostro pintara un rectangulo para delimitar el tamaño
#del rostro

while True: 
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = fade_cascade.detectMultiScale(gray, 1.1, 4)
    print(faces)
    
    #Al pintar un recuadro alrededor de la cara se laguea demasiado por mi procesador
    #for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow('Proyecto Final', img)
    #Al clikear la tecla esc se cierra el programa
    k = cv2.waitKey(30)
    if(k == 27):
        break

cap.release()