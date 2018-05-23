import speech_recognition as sr
r = sr.Recognizer()

def speech2text():
    
     with sr.Microphone() as source:
          r.energy_threshold = 47
          #r.adjust_for_ambient_noise(source)
          r.dynamic_energy_threshold = False
          print(r.energy_threshold)
          audio = r.listen(source, timeout= None, phrase_time_limit=5 )
          

     try:
          text = r.recognize_google(audio, language="de-De")
     except:
          text="except"
          pass
     
     return text
