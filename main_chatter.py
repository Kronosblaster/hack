import random
import nltk
from nltk.stem.porter import PorterStemmer
import pyjokes
nltk.download('punkt', quiet=True)
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', "english_rp")
corpus={

    'greet':[
        ["hi","hey","hello"],
        ["Hello:)","Hey there!","Hi, how are you?","What's up?"]
        ],

    'leave':[
        ["goodbye","exit","quit","bye","i'm leaving"],
        ["Thanks for visiting, see you later","Bye! Have a nice day:)","Bye! Come again soon"]
        ],
    
    'sad':[
        ["depressed","sad","distress","depress","depression","down"],
        ["joke","cat","pyjoke"]
        ],
    
    'fear':[
        ["fear","afraid","scared","scary","nervous"],
        ["<Say no to fear>"]
        ],

    'demotivated':[
        ["demotivated","bored","wasted","demoralised","demoralized","bore"],
        ["<insert inspirational quotes>"]
        ],

    'stress':[
        ["burnout","stress","stressed"],
        ["<Take a chill pill>"]
    ],

    'joke':[
        ["joke","funny","laugh"],
        ["joke","joke","joke","pyjoke"]
    ],

    'medical':{
        "depression":[],
        "anxiety":[],
        "fear":[],
        }
    }
jokes=[
    "A perfectionist walked into a bar...apparently, the bar wasn’t set high enough!",
    "I own the world's worst thesaurus. Not only is it awful, it's awful.",
    "The world tongue-twister champion just got arrested. I hear they're gonna give him a really tough sentence.",
    "What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus.",
    "I invented a new word!\nPlagiarism!",
    "Did you hear about the claustrophobic astronaut?\nHe just needed a little space.",
    "Why did the chicken run across the road?\nTo get to the other side faster.",
]

#main function
def main():
    flag=0

    while flag==0:
            print(">")
            cmd=takeCommand()
            cmd_tokenized=tokenize(cmd)
            cmd_stemmed=stem(cmd_tokenized)+cmd_tokenized
            #print(cmd_stemmed)
            if check(cmd_stemmed,corpus['leave'][0]):#exit
                flag=exit(corpus['leave'][1])

            elif check(cmd_stemmed,corpus['greet'][0]):
                greet_response(corpus['greet'][1])

            elif check(cmd_stemmed,corpus['sad'][0]):
                sad_response(corpus['sad'][1])

            elif check(cmd_stemmed,corpus['demotivated'][0]):
                demotivated_response(corpus['demotivated'][1])

            elif check(cmd_stemmed,corpus['stress'][0]):
                stress_response(corpus['stress'][1])

            elif check(cmd_stemmed,corpus['joke'][0]):
                joke_response(corpus['joke'][1])

            elif cmd_stemmed==['none', 'None']:
                print("...")

            else:
                #print("I don't know how I can help :(")
                say("I don't know how I can help")



#functions for user interaction
def greet_response(array):
    #print(random_gen(array))
    say(random_gen(array))

def exit(array):
    #print(random_gen(array))
    say(random_gen(array))
    return 1

def sad_response(array):
    foo=random_gen(array)
    if foo=="cat":
        say("Here's a cute cat!")
        print("A cat: (*w*)")

    if foo=="joke":
        #print("Joke time!")
        say("Joke time!")
        joke()

    if foo=="pyjoke":
        #print("Joke time!")
        say("Joke time!")
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
        say(My_joke)

def demotivated_response(array):
    #print(random_gen(array))
    say(random_gen(array))

def stress_response(array):
    #print(random_gen(array))
    say(random_gen(array))

def medical_response(array):
    print(random_gen(array))

def joke_response(array):
    foo=random_gen(array)

    if foo=="joke":
        #print("Joke time!")
        say("Joke time!")
        joke()

    if foo=="pyjoke":
        #print("Joke time!")
        say("Joke time!")
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
        say(My_joke)


#functions for program function
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
    
def stem(words):
    stemmer=PorterStemmer()
    foo=[stemmer.stem(w) for w in words]
    return foo

def random_gen(array):
    return array[random.randint(0, len(array)-1)]

def check(words,keys):
    for j in range(len(words)):
        for i in range(len(keys)):
            if words[j]==keys[i]:
                return True
    return False

def joke():
    #print(random_gen(jokes))
    say(random_gen(jokes))


def takeCommand():
         
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def say(text):
    engine.say(text)
    engine.runAndWait()
main()


