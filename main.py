print("Inintialsing sophie..")
from Speech import speak
import os
username=os.getlogin()
import random
import time
from sophie import sophie
#from speech2text import speech2text

print("sophie inintialised..")
print("\n")
    
def main():
    speak("Hallo "+ username+"!")
    while 1:
        input_string = input('Sophie :')  #modify       
        
        #input_string=speech2text()
        
        print (input_string)
        if input_string:
            input_string = input_string.lower()
            sophie(input_string)

if __name__ == "__main__":
    main()

