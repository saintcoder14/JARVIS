import pyttsx3  #for output voice kinda
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    # Imp function used to convert a text into audio
    engine.say(audio)
    engine.runAndWait()

def take_command():
    # takes in audio from microphone and returns string as o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said:{query}\n")
    except Exception:
       speak("Please, say that again")
       return "None"
    return query

def wish_me():
    #func to wish me on the basis of 'hour'
    print("Welcome Back, sir")
    speak("Jarvis, at your Service Sir!")
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour <12:
        speak("Good Morning darling")
    elif hour>=12 and hour <5:
        speak("Good afternoon darling")
    else: 
        speak("Good evening darling")
    speak("How may I help u?")

if __name__ == "__main__":
    # main function
    wish_me()
    while True:
        query=take_command().lower()
        if 'wiki' in query:
            speak('Searching Wikipedia')
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #elif 'what is the time' or 'whats the time' in query:
        #    strtime=datetime.datetime.now()
        #    speak("Sir, the time is %d %d" %(strtime.hour,strtime.minute))
                
        elif 'who is your master' in query:
            speak('It is one and only Master Sammridh')

        elif 'okay bye' or 'bye'  in query:
            exit()
        

