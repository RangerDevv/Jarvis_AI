from datetime import datetime
import speech_recognition as sr
import datetime

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()


# Reading Microphone as source
# listening the speech and store in audio_text variable
while True:
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print(r.recognize_google(audio_text))
        if r.recognize_google(audio_text)=="what is your name":
            print("My name is Jarvis, Your personal assistant")
        elif  r.recognize_google(audio_text)=="quit":
            break
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling


