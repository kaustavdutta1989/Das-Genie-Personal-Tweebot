import pyttsx3
import datetime
import speech_recognition
from chatterbot import ChatBot  # import the ChatterBot

# Chat-bot with Name
DasGenieBot = ChatBot('DasGenie')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)

def speak(audio):
    print("DasGenie: " + str(audio))
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am DasGenie. Ready to Serve!")

def takeCommand():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said = " +query.toString())

    except Exception as e:
        print("Say That Again, Please")
        return "None"
    return query

def getCommandResponse(userInput):

    exitCodes = ["bye", "exit", "chao"]
    for eCode in exitCodes :
        if(userInput.lower() == eCode):
            speak("Ok! I will Take a Nap")
            exit()
    return DasGenieBot.get_response(userInput.lower())
