print("Inintialsing sophie..")
from Speech import speak
import os
username=os.getlogin()
import random
import time
from sophie import sophie
print("sophie inintialised..")
print("\n")
    
def main():
    speak("Hallo "+ username+"!")
    while 1:
        input_string = input('Sophie :')  #modify
        if input_string:
            
            input_string = input_string.lower()
            sophie(input_string)

if __name__ == "__main__":
    main()

