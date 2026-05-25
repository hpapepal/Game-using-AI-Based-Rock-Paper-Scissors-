# ==========================================
# AI VIRTUAL ASSISTANT USING PYTHON
# ==========================================

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


# ==========================================
# INITIALIZE SPEECH ENGINE
# ==========================================

engine = pyttsx3.init()

engine.setProperty('rate', 170)


# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text):

    print("Assistant:", text)

    engine.say(text)

    engine.runAndWait()


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:

        return ""


# ==========================================
# START ASSISTANT
# ==========================================

speak("Hello! I am your AI Virtual Assistant.")


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    command = listen()


    # ==========================================
    # OPEN GOOGLE
    # ==========================================

    if "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")


    # ==========================================
    # OPEN YOUTUBE
    # ==========================================

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")


    # ==========================================
    # TELL TIME
    # ==========================================

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        speak(f"The current time is {current_time}")


    # ==========================================
    # ASK ABOUT AI
    # ==========================================

    elif "what is ai" in command:

        speak("Artificial Intelligence is the simulation of human intelligence by machines.")


    # ==========================================
    # EXIT COMMAND
    # ==========================================

    elif "exit" in command or "stop" in command:

        speak("Goodbye!")

        break


    # ==========================================
    # UNKNOWN COMMAND
    # ==========================================

    elif command != "":

        speak("Sorry, I did not understand that.")