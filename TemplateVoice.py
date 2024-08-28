import speech_recognition as sr
import pyttsx3

vocecita = pyttsx3.init()

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
        
    return command

while True:
    microfonito()