import speech_recognition as sr
r = sr.Recognizer()

def speech2text():
    
     with sr.Microphone() as source:
          r.energy_threshold = 47
          #r.adjust_for_ambient_noise(source)
          #r.dynamic_energy_threshold = False
          print(r.energy_threshold)
          try:
               audio = r.listen(source, timeout=0.5, phrase_time_limit=5 )
          except:
               pass

     try:
          text = r.recognize_google(audio, language="de-De")
     except:
          text="fehler"
          pass
     
     return text
