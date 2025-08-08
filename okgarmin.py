import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
import pygame
import os
import keyboard

#the 60 (on line 34 and 42) indicates the percentage treshold you need to cross for it to work (with the speech to text),
#lower percentage will make it easier to use it but it might also cause accidental use
#made by Federico_q. you can contact me at fquadrifoglio@gmail.com

did_you_activate_garmin = False
r = sr.Recognizer()
file_path1 = os.path.join(os.path.dirname(__file__), "okgarmin.mp3")
file_path2 = os.path.join(os.path.dirname(__file__), "videospeichern.mp3")

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(command)
    engine.runAndWait()

print("Listening...")

while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration = 0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            match1 = fuzz.ratio(MyText, 'ok garmin')
            match2 = fuzz.ratio(MyText, 'video station')
            if match1 >= 60: #////////here
                pygame.mixer.init()
                pygame.mixer.music.load(file_path1)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                pygame.mixer.quit()
                did_you_activate_garmin = True
            if match2 >= 60 and did_you_activate_garmin == True: #////////here
                pygame.mixer.init()
                pygame.mixer.music.load(file_path2)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                pygame.mixer.quit()
                keyboard.press_and_release('alt+f10') #adjust to whatever your clipping hotkey is
                did_you_activate_garmin = False
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass