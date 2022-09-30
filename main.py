from datetime import datetime
from urllib import response
import speech_recognition as sr
import pyttsx3

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
        resp = ""
        print(r.recognize_google(audio_text))
        if r.recognize_google(audio_text)=="what is your name":
            resp = "My name is Jarvis, Your personal assistant. How can I help?"
            SpeakText(resp)
        if  r.recognize_google(audio_text)=="quit":
            resp = "good day sir!"
            SpeakText(resp)
            break
        else:
            resp = "sorry, I dont understand."
            SpeakText(resp)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling


