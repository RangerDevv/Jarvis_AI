from datetime import datetime
from traceback import print_stack
from urllib import response
import speech_recognition as sr
import pyttsx3
import wikipedia as wp

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Reading Microphone as source
# listening the speech and store in audio_text variable

while True:
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print(r.recognize_google(audio_text))
        resp = ""
        if r.recognize_google(audio_text)=="what is your name":
            resp = "My name is Jarvis, Your personal assistant. How can I help?"
            SpeakText(resp)
        if  r.recognize_google(audio_text)=="quit":
            resp = "good day sir!"
            SpeakText(resp)
            break
        if  r.recognize_google(audio_text)=="who is Albert Einstein":
            search = wp.summary("Albert Einstein", sentences=4)
            SpeakText(search)
        else:
            resp = "sorry, I dont understand."
            SpeakText(resp)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
