import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

assistant_engine = pyttsx3.init()

def assistant_speak(audio_message) -> None:
    assistant_engine.say(audio_message)
    assistant_engine.runAndWait()

def get_current_time() -> None:
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    assistant_speak("The current time is")
    assistant_speak(current_time)
    print("The current time is", current_time)

def get_current_date() -> None:
    current_day = datetime.datetime.now().day
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    assistant_speak("The current date is")
    assistant_speak(current_day)
    assistant_speak(current_month)
    assistant_speak(current_year)
    print(f"The current date is {current_day}/{current_month}/{current_year}")

def greet_user() -> None:
    print("Welcome back, mam!!")
    assistant_speak("Welcome back, mam!!")

    current_hour = datetime.datetime.now().hour
    if 4 <= current_hour < 12:
        assistant_speak("Good Morning mam!!")
        print("Good Morning mam!!")
    elif 12 <= current_hour < 16:
        assistant_speak("Good Afternoon mam!!")
        print("Good Afternoon mam!!")
    elif 16 <= current_hour < 24:
        assistant_speak("Good Evening mam!!")
        print("Good Evening mam!!")
    else:
        assistant_speak("Good Night mam, See You Tomorrow")

    assistant_speak("Jarvis at your service mam, please tell me how may I help you.")
    print("Jarvis at your service mam, please tell me how may I help you.")

def capture_screenshot() -> None:
    screenshot_image = pyautogui.screenshot()
    screenshot_path = os.path.expanduser("~\\Pictures\\ss.png")
    screenshot_image.save(screenshot_path)

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic_source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio_input = recognizer.listen(mic_source)

    try:
        print("Recognizing...")
        voice_command = recognizer.recognize_google(audio_input, language="en-in")
        print(voice_command)
    except sr.UnknownValueError:
        assistant_speak("Sorry, I did not understand that.")
        return "Try Again"
    except sr.RequestError:
        assistant_speak("Sorry, my speech service is down.")
        return "Try Again"
    except Exception as error:
        print(error)
        assistant_speak("Please say that again")
        return "Try Again"

    return voice_command

if __name__ == "__main__":
    greet_user()
    while True:
        user_command = listen_to_command().lower()

        if "time" in user_command:
            get_current_time()

        elif "date" in user_command:
            get_current_date()

        elif "who are you" in user_command:
            assistant_speak("I'm JARVIS and I'm a desktop voice assistant.")
            print("I'm JARVIS I'm a desktop voice assistant.")

        elif "how are you" in user_command:
            assistant_speak("I'm fine mam, What about you?")
            print("I'm fine mam, What about you?")

        elif "fine" in user_command or "good" in user_command:
            assistant_speak("Glad to hear that mam!!")
            print("Glad to hear that mam!!")

        elif "wikipedia" in user_command:
            try:
                assistant_speak("Ok wait mam, I'm searching...")
                search_query = user_command.replace("wikipedia", "")
                wiki_result = wikipedia.summary(search_query, sentences=2)
                print(wiki_result)
                assistant_speak(wiki_result)
            except:
                assistant_speak("Can't find this page mam, please ask something else")

        elif "open youtube" in user_command:
            wb.open("youtube.com")

        elif "open google" in user_command:
            wb.open("google.com")

        elif "open stack overflow" in user_command:
            wb.open("stackoverflow.com")

        elif "play music" in user_command:
            music_directory = os.path.expanduser("~\\Music")
            music_files = os.listdir(music_directory)
            print(music_files)
            random_song_index = random.randint(0, len(music_files) - 1)
            os.startfile(os.path.join(music_directory, music_files[random_song_index]))

        elif "open chrome" in user_command:
            chrome_executable_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_executable_path)

        elif "search on chrome" in user_command:
            try:
                assistant_speak("What should I search?")
                print("What should I search?")
                chrome_search_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                chrome_search_query = listen_to_command()
                wb.get(chrome_search_path).open_new_tab(chrome_search_query)
                print(chrome_search_query)
            except Exception as search_error:
                assistant_speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")

        elif "remember that" in user_command:
            assistant_speak("What should I remember?")
            memory_data = listen_to_command()
            assistant_speak("You said me to remember that " + memory_data)
            print("You said me to remember that " + str(memory_data))
            with open("data.txt", "w") as memory_file:
                memory_file.write(memory_data)

        elif "do you remember anything" in user_command:
            with open("data.txt", "r") as memory_file:
                assistant_speak("You told me to remember that " + memory_file.read())
                print("You told me to remember that " + memory_file.read())

        elif "screenshot" in user_command:
            capture_screenshot()
            assistant_speak("I've taken a screenshot, please check it")

        elif "offline" in user_command:
            quit()
