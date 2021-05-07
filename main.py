import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# engine.say("Kuina")
# engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Kuina is listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        kuina = ['hey kuina','hey uwi na','hey queena','hey quina','hey cuina']
        if command in kuina:
            engine.say("yes?")
            engine.runAndWait()
            print(command)
except:
    pass