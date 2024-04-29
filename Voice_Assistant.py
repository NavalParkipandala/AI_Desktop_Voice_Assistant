import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import random
import webbrowser
import pyjokes
import time
import subprocess
import pyautogui
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio=r.listen(source, timeout=1, phrase_time_limit=6)
    try:
        print('Recognizing.....')
        query=r.recognize_google(audio, language='en-in')
        print(f'user said {query}')
    except Exception as e:
        speak('unable to recognize your voice')
        return 'None'
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('hi, good morning sir')
    elif hour>=12 and hour<18:
        speak('hi, good afternoon sir')
    else:
        speak('hi, good evening sir')

    speak('i am your voice assistant sam')

def username():
    speak('what should i call you sir?')
    uname=takecommand()
    speak(f'welcome mister {uname}')
    speak(f'what should i help you {uname} sir?')


if __name__ == '__main__':
    wishme()
    username()
    
    while True:
        order=takecommand().lower()
        
        if 'what is your name' in order:
            speak('my riends call me sam')

        elif 'how are you' in order:
            speak('i am fine, thank you')
            speak('how are you sir?')

        elif 'fine' in order or 'good' in order:
            speak('its good to know that you are fine sir')

        elif 'who i am' in order:
            speak('if you can talk, then you are definately an human being')

        elif 'love' in order:
            speak('it is &th sense that destroyes all other senses')

        elif 'i love you' in order:
            speak('oh my god thank you, i love you too')

        elif 'will you be my girlfriend' in order:
            speak('oh my god what is this, i will think about it, may you give me some more time to think')

        elif 'open notepad' in order:
            npath='C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'wikipedia' in order:
            speak('searching....')
            repl=order.replace('wikipedia', "")
            results=wikipedia.summary(order, sentences=1)
            speak(results)

        elif 'play music' in order or 'play songs' in order:
            music_dir='D:\\songs\\songstelugu'
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'open google' in order:
            speak('here you go to google sir!')
            webbrowser.open('google.com')

        elif 'open chrome' in order:
            speak('here you go to chrome sir!')
            webbrowser.open('chrome.com')

        elif 'open youtube' in order:
            speak('here you go to youtube sir!')
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in order:
            speak('here you go to stackoverflow sir!, happy coding')
            webbrowser.open('stackoverflow.com')

        elif 'amazon' in order:
            speak('here you go to amazon sir!, happy shopping')
            webbrowser.open('amazon.in')

        elif 'myntra' in order:
            speak('here you go to myntra sir!, happy shopping')
            webbrowser.open('myntra.com')

        elif 'joke' in order:
            speak(pyjokes.get_joke(language='en', category='neutral'))

        elif 'the time' in order:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(strtime)

        elif 'shutdown' in order or 'power off' in order or 'turn off' in order:
            speak('hold on a second sir, your system is on its way to shutdown')
            speak('make sure that all of your apps are closed')
            time.sleep(5)
            subprocess.call(['shutdown', '\s'])

        elif 'restart' in order:
            speak('restarting...')
            subprocess.call(['shutdown', '\r'])

        elif 'hybernate' in order:
            speak('hybernating..')
            subprocess.call(['shutdown'], '\h')

        elif 'log out' in order or 'sign out' in order:
            speak('please make sure that all of your apps are closed')
            subprocess.call(['shutdown', '\i'])

        elif 'swich window' in order or 'another window' in order or 'change window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'write a note' in order:
            speak('what should i write sir?')
            note=takecommand()
            file=open('naval.txt', 'w')
            speak('should i include date and time as well sir?')
            if 'yes' in order or 'yeah' in order or 'definately' in order or 'sure' in order:
                strtime=datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strtime)
                file.write(note)
                speak('done sir')
            else:
                file.write(note)
                speak('done sir')

        elif 'show note' in order or 'show notes' in order:
            file=open('naval.txt', 'r')
            print(file.read())
            speak(file.read(6))

        elif 'bmi' in order:
            speak('please tell me your height in centimeteres sir')
            height=takecommand()
            speak('please tell me your weight in kilograms sir')
            weight = takecommand()
            height=float(height)/100
            bmi=float(weight)/(height*height)
            speak(f'your body mass index is {bmi}')
            if (bmi>0):
                if (bmi<=16):
                    speak('you are severly underweight sir')
                elif (bmi<=18.5):
                    speak('you are underweight sir')
                elif (bmi<=25):
                    speak('you are healthy')
                elif (bmi<=30):
                    speak('you are overweight sir')
                else:
                    speak('you are severly overweight sir')
            else:
                speak('please tell me valid height and weight sir')

        elif 'exit' in order or 'quite' in order or 'good by' in order:
            speak('thank you so much for remembering me sir, have a good day')
            sys.exit()