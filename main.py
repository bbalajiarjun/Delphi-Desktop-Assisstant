import pyttsx3;
import speech_recognition as sr;
import datetime;
import wikipedia;
import webbrowser;
import os;
import smtplib;

print("Initializing Delphi...");

MASTER = "Arjun";

engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[1].id);

# Speak Function will pronounce the string which is passed to it
def speak(text):
    engine.say(text);
    engine.runAndWait();
#This function will wish you as per the current time
def wishme():
    hour = int(datetime.datetime.now().hour);

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER);

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER);

    else:
        speak("Good Evening" + MASTER);
    speak("I am the oracle of Delphi. What Prophecy Shall I reveal")

    #speak("I am the Oracle of Delphi. How may I be at your service today?")
#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        print("Listening...");
        audio = r.listen(source);
    try:
        print("Recognizing");
        query = r.recognize_google(audio, language = 'en-us');
        print(f"user said: {query}\n");
    except Exception as e:
        print("Say that again please");
        query = None;
    return query

def speak_and_write(text):
    print(text);
    speak(text);
# Main Program
speak("Initializing Delphi...");
wishme();
query = takeCommand();

#Logic for executing basic Tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...');
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences = 2)
    print(results);
    speak(results);

elif 'open youtube' in query.lower():
    #webbrowser.open("youtube.com");
    url = "youtube.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s';
    webbrowser.get(chrome_path).open(url, new = 2);

elif 'open google' in query.lower():
    #webbrowser.open("google.com");
    url = "google.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s';
    webbrowser.get(chrome_path).open(url, new = 2);

elif 'open stackoverflow' in query.lower():
    #webbrowser.open("stackoverflow.com");
    url = "stackoverflow.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s';
    webbrowser.get(chrome_path).open(url, new = 2);

elif 'open github' in query.lower():
    #webbrowser.open("github.com");
    url = "github.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s';
    webbrowser.get(chrome_path).open(url, new = 2);

# elif 'play music on Spotify' in query.lower():
#     songsPath = "C:\\Users\\bbala\\AppData\\Local\\packages\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\LocalState\\Spotify\\Storage";
#     os.startfile(songsPath);

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}");










