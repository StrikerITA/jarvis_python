# referenze libreria: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
import os
import pyttsx3
import speech_recognition as sr

if __name__ == '__main__':
    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure: ")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print("Jarvis ha capito: \n", text)

        if text.find('apri spotify')!=0 :
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Spotify\Spotify.lnk"
            os.startfile(path)
        if text.find('chi sono')!=0 :
            path = "www.instagram.com/andrea._.riccardi/"
            os.startfile(path)

    except Exception as e:
        print(e)
