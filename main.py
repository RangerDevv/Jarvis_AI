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

Questionwords = [
    "who is",
    "what is",
    "what are"
]

while True:
    SpeakText("Hello sir, how may I help u?")
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        # print(r.recognize_google(audio_text))
        command = r.recognize_google(audio_text)
        resp = ""
        if command=="what is your name":
            resp = "My name is Jarvis, Your personal assistant. How can I help?"
            SpeakText(resp)
        if  command=="quit":
            resp = "good day sir!"
            SpeakText(resp)
            break
        if  "who is" or "what is" or "what are" in command:
            search = command.replace( "who is" or "what is" or "what are" ," ")
            result = wp.summary(search , 4)
            SpeakText(result)
        else:
            resp = "sorry, I dont understand."
            SpeakText(resp)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
