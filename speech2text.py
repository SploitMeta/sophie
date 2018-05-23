import speech_recognition as sr
r = sr.Recognizer()

def speech2text():

    try:
        with sr.Microphone() as source:
            print ('Say Something!')
            audio = r.listen(source)
            print ('Done!')
         
        text = r.recognize_google(audio, language="de-De")
    
    except:
        text=""
        pass
    
    return text
