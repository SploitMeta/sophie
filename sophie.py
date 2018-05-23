import os
import time, datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from Speech import speak


def sophie(string):

    #Splitting each sentence in a list of words.
    word_list = word_tokenize(string)

    #Setting up stop_words: words that are redundant.
    stop_words = set(stopwords.words('german'))

    #Creating space for a list of sentences without stop_words.
    if "search" not in word_list and "google" not in word_list and "say" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
                filtered_sentence = [w for w in word_list]
  

    if "hello" in filtered_sentence:
        speak("Hallo " + username)

    elif "tschüss" in filtered_sentence:
        speak("Bis dann " + username + "!")
        quit()

    elif "time" in filtered_sentence:
        print(time.ctime())

    elif "say" in filtered_sentence:
        output = ' '.join(filtered_sentence[1:])
        speak(output)

        



        
    return None


from main import username

