"""
Speaks input string using the internet.
"""
from gtts import gTTS
import os
from playsound import playsound

def speak(out_string):
    """
    Speaks using gTTs from the internet.
    """
    path = os.getcwd() + "/Text_Files/ping_result.txt"
    path_os = path.replace(" ", "\ ")
    path_os = path_os.replace("(", "\(")
    path_os = path_os.replace(")", "\)")
    tts = gTTS(text = out_string, lang = 'de')
    tts.save("soundfile.mp3")
    print("Sophie: " + out_string)
    os.system("mpg123 -q soundfile.mp3")
  
