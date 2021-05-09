import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import winshell
import wolframalpha

engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.setProperty('volume',5.0) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is : ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    print(".....................................................")
    print(".......................Rio Robot ....................")
    print(".....................................................")
    # time()
    # date()
    # Greeting
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir!!!!!!")
    speak("Rio at your service.Please tell me how can i help you today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............................................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconizing...........................................")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print(".....................................................")
        print("....................Say something....................")
        print(".....................................................")
        return "None"
    return query

def cpu():
    print(".....................................................")
    print(".........................Cpu.........................")
    print(".....................................................")
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    print('CPU is at     :', usage)
    print("Battery is at :", battery.percent)
    speak('CPU is at' + usage)
    speak("Battery is at")

    speak(battery.percent)

def joke():
    print(".....................................................")
    print(".........................joke........................")
    print(".....................................................")
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishme()
    while True:
        query = TakeCommand().lower()  # all command stored in lower Case
        if 'time' in query:  # tell us time
            print(time())
            time()


        elif 'date' in query:  # tell us date
            print(date())
            date()

        elif 'wikipedia' in query:  # find in wikipedia
            import wikipedia
            speak("Searching")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(".....................................................")
            print("......................wikipedia......................")
            print(".....................................................")
            print(result)
            speak(result)

        elif 'joke' in query:
            joke()




        elif 'chrome' in query:  # Open chrome
            print(".....................................................")
            print("........................chrome.......................")
            print(".....................................................")
            speak("What should I search?")
            print("What should I search?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:  # Open chrome
            print(".....................................................")
            print("...................search youtube....................")
            print(".....................................................")
            speak("What should I search?")
            print("What should I search?")
            search_terms = TakeCommand().lower()
            speak("Here i go to youtube")
            wb.open('https://www.youtube.com/results?search_query='+search_terms)

        elif 'search google' in query:  # Open chrome
            print(".....................................................")
            print("...................search google.....................")
            print(".....................................................")
            speak("What should I search?")
            print("What should I search?")
            search_terms = TakeCommand().lower()
            speak("Here i go to Google")
            wb.open('https://www.google.com/search?q='+search_terms)

        elif 'cpu' in query:  # Open cpu
            cpu()

        elif 'go offline' in query:  # Open cpu
            speak("Going offline Sir")
            quit()

        elif 'how are you' in query:  # Open cpu
            speak("I am fine and you?")


        elif 'founder of bangladesh' in query:  # Open cpu
            speak("Sheikh Mujibur Rahman")

        elif 'how are you' in query:  # Open cpu
            speak("I am fine and you?")

        elif 'who are you' in query:  # Open cpu
            speak("I am Rio")


        elif 'word' in query:  # Open cpu
            print(".....................................................")
            print("........................word.........................")
            print(".....................................................")
            speak("Opening word sir")
            msword = 'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(msword)

        elif 'write a note' in query:
            print(".....................................................")
            print(".....................write a note....................")
            print(".....................................................")
            speak("What should i write,Sir?")
            notes = TakeCommand()
            file = open('file.txt','w')
            file.write(notes)
            speak("Done taking Note Sir")

        elif 'my note' in query:
            print(".....................................................")
            print(".....................Your Note is ...................")
            print(".....................................................")
            speak('Your Note is : ')
            file = open('file.txt','r')
            print(file.read())

        elif 'screenshot' in query:
            print(".....................................................")
            print("....................screenshot Done .................")
            print(".....................................................")
            pyautogui.hotkey('win','printscreen')
            speak('Done Sir')

        elif 'folder' in query:
            print(".....................................................")
            print("....................screenshot Open .................")
            print(".....................................................")
            pyautogui.hotkey('win','printscreen')
            msword = 'C:/Users/riyad/Pictures/Screenshots'
            os.startfile(msword)
            speak('open  Sir')

        elif 'play music' in query:
            print(".....................................................")
            print("......................play music ....................")
            print(".....................................................")
            speak("Opening Music sir")
            music = 'C:\Music\m.mp3'
            os.startfile(music)

        elif 'open youtube' in query:
            speak('okay')
            wb.open('www.youtube.com')

        elif 'open facebook' in query:
            speak('okay')
            wb.open('www.facebook.com')

        elif 'mujibur' in query:
            print('Bangladeshi politician and statesman. He is called the "Father of the Nation" in Bangladesh. He served as the first President of Bangladesh and later as the Prime Minister of Bangladesh from 17 April 1971 until his assassination on 15 August 1975.')
            speak('Bangladeshi politician and statesman. He is called the "Father of the Nation" in Bangladesh. He served as the first President of Bangladesh and later as the Prime Minister of Bangladesh from 17 April 1971 until his assassination on 15 August 1975.')

        elif 'Mujeeb' in query:
            print('Bangladeshi politician and statesman. He is called the "Father of the Nation" in Bangladesh. He served as the first President of Bangladesh and later as the Prime Minister of Bangladesh from 17 April 1971 until his assassination on 15 August 1975.')
            speak('Bangladeshi politician and statesman. He is called the "Father of the Nation" in Bangladesh. He served as the first President of Bangladesh and later as the Prime Minister of Bangladesh from 17 April 1971 until his assassination on 15 August 1975.')

        elif 'open google' in query:
            speak('okay')
            wb.open('www.google.co.in')
#Call
        elif 'call momin' in query:
            import time
            speak('okay')
            wb.open('www.facebook.com/videocall/incall/?peer_id=100011289311257&call_id=3150416261&is_caller=true&audio_only=true&nonce=t94ksj4fux98&initialize_video=false')
            time.sleep(9)
            pyautogui.doubleClick(x=480, y=690)
            print("Calling")

        elif 'call Ronnie' in query:
            import time
            speak('okay')
            wb.open('www.facebook.com/videocall/incall/?peer_id=100008272471280')
            time.sleep(5)
            pyautogui.doubleClick(x=480, y=690)
            print("Calling")



        elif 'creator' in query:
            speak("Riyadh")

        elif 'open meet' in query:
            speak('okay')
            wb.open('meet.google.com')

        elif 'open gmail' in query:
            speak('okay')
            wb.open('www.gmail.com')

        elif 'about momin' in query:
            print('momin is your best fiend. He is from Dhaka Gazipur.He is also food lover')
            speak('momin is your best fiend. He is from Dhaka Gazipur.He is also food lover.Friendships are born in a million different ways, and all good friends strive to achieve the same goal: to be a source of love and support')

        elif 'shutdown' in query:
            speak('okay')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('enter')

        elif 'auto like' in query:
            import time
            speak('okay Auto like Start')
            number = [1, 2, 4]
            pyautogui.click(x=10, y=908)
            pyautogui.press('f5')
            time.sleep(5)
            print(".....................................................")
            print("....................Timeline react...................")
            print(".....................................................")
            for i in range(5):
                #  while keyboard.is_pressed('t') == False:
                time.sleep(2)
                pyautogui.press('j')
                time.sleep(1)
                pyautogui.press('l')
                time.sleep(1)
                print(".....................................................")
                print("..........Timeline react:", i + 1, " Times...................")
                print(".....................................................")
                for i in range(random.choice(number)):
                    pyautogui.press('right')
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(x=10, y=908)

        elif 'auto comment' in query:
            import time
            speak('okay comments Start')
            comments = ["Nice", "wow", "joss", "excellent", "superior", "good"]
            pyautogui.click(x=10, y=908)
            pyautogui.press('f5')
            time.sleep(5)
            print(".....................................................")
            print("..................Timeline Comments..................")
            print(".....................................................")
            for i in range(1):
                # while keyboard.is_pressed('t') == False:
                time.sleep(1)
                for i in range(5):
                    #    while keyboard.is_pressed('t') == False:
                    time.sleep(2)
                    pyautogui.press('j')
                    time.sleep(1)
                    pyautogui.press('c')
                    time.sleep(5)
                    pyautogui.typewrite(comments[i % 6])
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.click(x=10, y=908)
                    print(".....................................................")
                    print("..........Timeline Comments", i + 1, " Times.................")
                    print(".....................................................")

        elif 'han han' in query:
            speak('okay Haha react Start')
            import time
            number = [3]
            pyautogui.click(x=10, y=908)
            pyautogui.press('f5')
            time.sleep(5)
            print("................Timeline react(Haha)................")
            for i in range(5):
              #  while keyboard.is_pressed('t') == False:
                    time.sleep(2)
                    pyautogui.press('j')
                    time.sleep(1)
                    pyautogui.press('l')
                    time.sleep(1)
                    print("...............Timeline react", i + 1, " Times...............")
                    for i in range(random.choice(number)):
                        pyautogui.press('right')
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.click(x=10, y=908)
        elif 'invite' in query:
            import time
            speak("Oke Sir ")
            time.sleep(5)
            print("................Invite Group................")
            for i in range(9999):
             #   while keyboard.is_pressed('t') == False:
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.press('enter')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    print("...............Invite :", i + 2, " Times...............")
                    time.sleep(1)
                #    break
            print("...............Invite Stop...............")

        elif 'love react' in query:
            import time
            number = [1]
            pyautogui.click(x=10, y=908)
            pyautogui.press('f5')
            time.sleep(5)
            print("................Timeline react(Love)................")
            for i in range(5):
              #  while keyboard.is_pressed('t') == False:
                    time.sleep(2)
                    pyautogui.press('j')
                    time.sleep(1)
                    pyautogui.press('l')
                    time.sleep(1)
                    print("...............Timeline react", i + 1, " Times...............")
                    for i in range(random.choice(number)):
                        pyautogui.press('right')
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.click(x=10, y=908)

        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
            except:
                speak("Recycle Bin already empty")
                TakeCommand()
        elif "what is your name" in query:
            speak("Rio 2.0")

        elif "what is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()


        elif "where is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "who is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "where we are actually right now" in query:
            try:
                speak("Kurigram , Rangpur ,Bangladesh")
            except:
                print("No results")
                TakeCommand()



        elif "how" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "can" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "who" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "do you" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()



        # calculation
        elif "calculate" in query:
            try:
                app_id = "7PLQXV-UVR3WQPTYU"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except:
                TakeCommand()



        elif "creator" in query:
            speak("Riyadh")

        elif "introduce yourself" in query:
            speak("I am Rio 1.0 , Personal AI assistant , "
                  "I am created by Riyadh ")



















