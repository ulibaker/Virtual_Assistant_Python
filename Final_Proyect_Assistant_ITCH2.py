import cv2
import speech_recognition as sr
import pyttsx3


#INCIO DE LAS VARIABLES NECESARIAS PARA EL FUNCIONAMIENTO DEL PROGRAMA
vocecita = pyttsx3.init()
fade_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#FUNCION QUE RECIBE UN TEXTO COMO PARAMETRO Y EL ASISTENTE VIRTUAL LO DIRA
def habla(text):
    vocecita.say(text)
    vocecita.runAndWait()

#FUNCION QUE SE UTILIZA PARA RECIBIR UNA ENTRADA CON EL MICROFONO
#LA PROCESA Y LA DEVUELVE COMO UN STRING LISTO PARA USARSE
def microfonito():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio,language='ES')
        habla(command)
    
    except sr.UnknownValueError:
            habla("Hubo un error en reconocer tu voz")
            return microfonito()
    return command.lower()

#FUNCION QUE SE UTILIZABA PARA SABER LA INFORMACION DE LAS CARRERAS
def informacion_carreras():
    
    bool_carrera = False
        
    while(not bool_carrera):
        
        habla("¿Sobre cual carrera te gustaria tener conocimiento?")
        
        carrera = microfonito()
        
        print(carrera)
        
        #Ingeniería en Sistemas Computacionales
        if 'ingeniería en sistemas' in carrera or 'sistemas' in carrera:
            habla("La encargada es Juanis Sarmiento")
            habla("Su correo es: coord_isc_iinf@chihuahua2.tecnm.mx")
            bool_carrera = True
        
        #Ingeniería Informática
        elif 'ingeniería informática' in carrera or 'informática' in carrera:
            habla("La encargada es Juanis Sarmiento")
            habla("Su correo es: coord_isc_iinf@chihuahua2.tecnm.mx")
            bool_carrera = True
            
        #Ingeniería Industrial
        elif 'ingeniería industrial' in carrera or 'industrial' in carrera:
            habla("La encargada es Lina Santos Benitez")
            habla("Su correo es: coord_ingindustrial@chihuahua2.tecnm.mx")
            bool_carrera = True
                
        #Ingeniería en Diseño Industrial
        elif 'ingeniería en diseño industrial' in carrera or 'ingeniería en diseño' in carrera or 'diseño industrial' in carrera or 'diseño' in carrera:
            habla("El encargado es Salvador Ortega")
            habla("Su correo es coord_disindustrial@chihuahua2.tecnm.mx")
            bool_carrera = True
                    
        #Ingeniería en Gestion Empresarial
        elif 'ingeniería en gestión empresarial' in carrera or 'ingeniería en gestión' in carrera or 'gestión empresarial' in carrera or 'gestión' in carrera:
            habla("La encargada es Merary Jimenez")
            habla("Su correo es: coord_admin_ige@chihuahua2.tecnm.mx")
            bool_carrera = True
        
        #Licenciatura en Administración
        elif 'licenciatura en administración' in carrera or 'administración' in carrera or 'admi' in carrera:
            habla("La encargada es Merary Jimenez")
            habla("Su correo es: coord_admin_ige@chihuahua2.tecnm.mx")
            bool_carrera = True
        
        #Arquitectura
        elif 'arquitectura' in carrera or 'arqui' in carrera:
            habla("La encargada es Citlalli Arreola Hernandez")
            habla("coord_arquitectura@chihuahua2.tecnm.mx")
            bool_carrera = True
            
        elif 'salir' in carrera or 'volver' in carrera:
            habla("Espero que la informacion le haya servido")
            bool_carrera = True
            
        else:
            habla("No puedo reconocer su petición")


##FUNCION QUE SE UTILIZA PARA DAR INFORMACION ACERCA DEL SERVICIO SOCIAL
def servicio_social():
    
    habla("Primeramente se necesita tener aprobado el 70 porciento de los creditos")
    habla("Se debe de asistir al curso de induccion obligatoriamente")
    habla("Debe de estar inscrito")
    habla("Y debes de contar con el seguro facultativo vigente")
    habla("Ademas es necesario cumplir con 500 horas en un periodo no menor a 6 meses")
    bool_servicio = False
    
    while(not bool_servicio):
        
        habla("¿Desea saber mas información?")
        
        servicio = microfonito()
        
        print(servicio)
        
        if "si" in servicio or "sí" in servicio or "afirmativo" in servicio:
            habla("Lo primero que se necesita es que el estudiante tenga un lugar ya definido en el cual va a realizar el servicio, ya teniendolo es necesario")
            habla("LLenar el formato de carta de compromiso, carta de asignacion, plan de trabajo y el formato de solicitud")
            habla("Toda esta papeleria debera llevarse al departamento de servicio social en las fechas correspondientes")
            habla("En caso de que la papeleria este en orden se le dara una carta de aceptacion y podra comenzar su servicio")
            
            habla("Una vez hecho esto, podras comenzar con tu servicio social")
            habla("Es importante recordar que cada dos meses deberas entregar tus documentos")
            habla("Los cuales son: autoevaluacion cualitativa, evaluacion cualitativa y el reporte bimestral")
            habla("Ademas de subir al moodle minimo 3 fotos para comprobar que en efecto se esta realizando el servicio social")
            
            habla("ATENCION")
            habla("Recuerda estar muy atento a las fechas que estara brindando el tecnologico")
            bool_servicio = True
        
        elif "no" in servicio or "negativo" in servicio:
            habla("Espero que la información recibida haya sido de ayuda")
            bool_servicio = True
        
        else:
            habla("No puedo reconocer su petición")

##FUNCION QUE SE UTILIZA PARA DAR INFORMACION ACERCA DE LAS RESIDENCIAS PROFESIONALES       
def residencias_profesionales():
    habla("Como requisitos no debe de contarse con ninguna asignatura en curso especial")
    habla("debe ternese acreditado el servicio social y las actividades complementarias")
    habla("debe haberse aprobado el 80 porciento de los creditos")
    habla("Y finalmente el alumno debe de estar inscrito")

    bool_residencias = False

    while(not bool_residencias):

        habla("Deseas saber mas informacion")
        
        residencias = microfonito()

        print(residencias)

        if "si" in residencias or "sí" in residencias or "afirmativo" in residencias:
            
            habla("Lo primero es tener un lugar en el cual se van a realiar")
            habla("Luego se debe elaborar el anteproyecto, llenar la solicitud de residencias y la empresa en cuestion debe de hacer una carta de aceptación")
            habla("Deben enviarse al correo de tu coordinador de carrera para que los analice")
            habla("En caso de que tengan errores, se te diran y debes corregirlos y volverlos a enviar")
            habla("Si ya estan correctos los datos, se enviara al departamento academico")
            habla("Una vez hecho esto , se realizara un convenio")
            habla("El estudiante debe de presentarse en el lugar de sus residencias para que sellen y firmen el convenio")
            habla("El estudiante debe de presentar copias del convenio y la carta de aceptacion a los siguientes departamentos")
            habla("Division de Estudios, Asesor interno, Gestion y Vinculacion y a la Empresa")
            habla("Al concluir las practicas debe de entregarse un reporte final, a division de estudios, asesor interno y area academica")
            
            bool_residencias = True
        
        elif "no" in residencias or "negativo" in residencias:
            habla("Espero que la información recibida haya sido de ayuda")
            bool_residencias = True
        
        else:
            habla("No puedo recconocer su petición")

##FUNCION QUE SE UTILIZA PARA DAR INFORMACION ACERCA DE LAS RESIDENCIAS PROFESIONALES
def titulacion():
    habla("Para comenzar con el proceso  de titulacion, se debio concluir con todos los creditos, creditos complementarios, servicio social y residencias profesionales")
    habla("Luego debes de iniciar el tramite llenando una solicitud en la pagina del tecnologico")
    habla("Debes de tener el formato de registro del proyecto, el cua debes solicitarlo con el jefe de oficina de tu carrera")
    habla("Sigue adjuntar el archivo en formato pdf del informe tecnico de residencias profesionales")
    habla("Luego sigue enviar el informe tecnico de residencias profesionales")
    habla("Todo esto debes de enviarlo al correo coord_titulacion@chihuahua2.tecnm.mx")
    habla("Despues de esto te enviaran la informacion correspondiente para continuar con el proceso")
    habla("Espero que la información recibida haya sido de ayuda")

##FUNCION PRINCIPAL EN DONDE VA A USARSE TODA LA INFORMACION
def principal():
   habla("Hola, ¿Sobre que te gustaria estar mas informado?")
   #habla("Di opción 1: Para conocer informacion sobre las carreras")
   #habla("Di opción 2: Para conocer informacion sobre el servicio social")
   #habla("Di opción 3: Para conocer informacion sobre las residencias profesionales")
   #habla("Di opción 4: Para conocer informacion sobre la titulacion")
   #habla("Di opción 5: Para salir")
   
   bool_opciones = False
   
   while(not bool_opciones):
       
       opciones = microfonito()
       
       #INFORMACION SOBRE LAS CARRERAS
       if "opción 1" in opciones or "opción uno" in opciones or "uno" in opciones:
           habla("informacion sobre las carreras")
           informacion_carreras()
           bool_opciones = True
       
       #INFORMACION SOBRE EL SERVICIO SOCIAL 
       elif "opción 2" in opciones or "opción dos" in opciones or "dos" in opciones:
           habla("Informacion sobre el servicio social")
           servicio_social()
           bool_opciones = True

        #INFORMACION SOBRE RESIDENCIAS PROFESIONALES   
       elif "opción 3" in opciones or "opción tres" in opciones or "tres" in opciones:
           habla("Informacion sobre residencias profesionales")
           residencias_profesionales()
           bool_opciones = True

        #INFORMACION SOBRE TITULACION   
       elif "opción 4" in opciones or "opción cuatro" in opciones or "cuatro" in opciones:
           habla("informacion sobre titulacion")
           titulacion()
           bool_opciones = True
        
        #OPCION PARA SALIR
       elif "opción 5" in opciones or "opción cinco" in opciones or "cinco" in opciones:
           habla("Adios, nos vemos pronto")
           bool_opciones = True
           
       else:
           habla("No puedo reconocer su peticion")
           bool_opciones = True
           principal()
     
   habla("Espero el asistente virtual le haya ayudado")

#FUNCION QUE SE UTILIZA PARA RECONOCIMIENTO FACIAL
#EN CASO DE ENCONTRAR UNA CARA, RETORNA VERDADERO PARA DAR SEGUIMIENTO AL PROGROMA
#DE LO CONTRARIO SE VUELVE A LLAMAR LA FUNCION
def reconocimiento():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = fade_cascade.detectMultiScale(gray, 1.1, 4)
    #cv2.imshow('Proyecto Final', img)
    
    longitud = len(faces)
    print(longitud)
    
    if(longitud):
        print(faces)
        habla("Se reconocio a una persona")
        return True
    
    else:
        habla("Por favor acerquese a la camara")
        return reconocimiento()
    
    cap.release()
    
##AQUI COMIENZA EL CODIGO QUE HACE FUNCIONAR EL CODIGO

#CODIGO QUE HACE QUE SE RECONOZCA UNA CARA Y DESPUES MANDA A LLAMAR
#LA FUNCION QUE UTILIZA EL MICROFONO PARA RECONOCER LA VOZ
while True:
    bool_okey = reconocimiento()
    if(bool_okey):
        principal()