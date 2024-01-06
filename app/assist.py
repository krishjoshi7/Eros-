import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# To store the to-do list
tasks = []

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  
    except Exception as e:
        print("Say that again, please...")
        return "None"

    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")    
    elif 12 <= hour < 18:
        speak("Good Afternoon!")       
    else:
        speak("Good Evening!")      

    speak('Hii Krishna, I am EROS, your personal assistant. Please tell me how may I help you')

def openWeb(url):
    webbrowser.open(url)

def playMusic():
    music_dir = 'https://link-to-your-playlist.com'  # Provide the link to your playlist
    songs = os.listdir(music_dir)
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def addTask(task):
    tasks.append({"task": task, "done": False})
    speak(f'Task "{task}" added to your to-do list.')

def showTasks():
    if not tasks:
        speak('Your to-do list is empty.')
    else:
        speak('Here is your to-do list:')
        for i, task_info in enumerate(tasks, start=1):
            status = "done" if task_info["done"] else "not done"
            speak(f'Task {i}: {task_info["task"]}, Status: {status}')

def markTaskDone(task_name):
    for task_info in tasks:
        if task_info["task"].lower() == task_name.lower():
            task_info["done"] = True
            speak(f'Task "{task_name}" marked as done.')
            return
    speak(f'Task "{task_name}" not found in your to-do list.')

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        # Check for the wake word to activate the assistant
        if 'hello eros' in query:
            wishMe()

            # Continue listening for and processing other commands
            while True:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=5) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query or 'open google' in query:
                    openWeb("youtube.com")

                elif 'play music' in query:
                    playMusic()

                elif 'add task' in query:
                    speak('Sure, what task would you like to add?')
                    task = takeCommand()
                    addTask(task)

                elif 'show tasks' in query:
                    showTasks()

                elif 'done task' in query:
                    task_name = query.split('done task', 1)[1].strip()
                    markTaskDone(task_name)

