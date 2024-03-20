import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def greeter():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        say("Good morning")
    elif hour>=12 and hour<18:
        say("Good Afternoon")
    else:
        say("Good Evening")
    say("I am your helper. How can I  help you? ")


def taskAssigning():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio,language= 'en-in' )
        print("Recognising")
        print(f"User:{task}\n")
    except Exception as e:
        say("Please can you repeat sir!!")
        return "None"
    return task

sites = [["youtube","youtube.com"],["google","google.com"],
["wikipedia","wikipedia.com"],["aerp login","youtube.com"],
["github","github.com"],["instagram","instagram.com"],
["linked in","linkedin.com"],["riplet","riplet.com"],
["online compiler","Online compiler"],["linkedin","linkedin.com"]]

def taskSolver(task):
    for site in sites:
        if (f"open {site[0]}") in task.lower():
            say(f"Opening {site[0]}")
            webbrowser.open(site[1])   
        elif (f"search") in task.lower():
            say(f"Searching")
            webbrowser.open(task)
        
if __name__ == "__main__":
    greeter()
    task = taskAssigning().lower()
    taskSolver(task)
