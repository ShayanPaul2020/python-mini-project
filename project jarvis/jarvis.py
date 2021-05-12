import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes

#setting the voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices[0].id)
# 0 is for david and 1 is for zara

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good mornig sir!')
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")        
    speak(" i'm jarvis. please tell me how may i help you ")
    speak('Mr shayan paul is my creator')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query




if __name__ == "__main__":
    wishme()
    
    while (1):
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open google map' in query:
            webbrowser.open("https://maps.google.com/")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'play music' in query:
            music_dir = 'D:\\favarite song'
            songs = os.listdir(music_dir)
            print(songs[0])    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'what is the time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")                         
        
        elif 'open anaconda navigator' in query:
            condaPath="C:\\Users\\shaya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)"
            os.startfile(condaPath)
        elif 'open code' in query:
            codePath = "C:\\Users\\shaya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open gmail' in query:
            webbrowser.open('Gmail.com') 

        elif 'joke' in query:
              speak(pyjokes.get_joke()) 
        elif 'stop' in query:
            break           
        