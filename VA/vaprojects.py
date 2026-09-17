'''
gTTs -->Google text to Speech -->pip install gtts
playsound -->pip install playsound==1.2.2
pyaudio -->pip install pyaudio
SpeechRecognation -->pip install SpeechRecognation

3 Functions-->1)Listen(SpeechRecognation)
           -->2)respond(ggts)
           -->3)Assistant(Condition) --->conversation,Greeting,datetime,
           locate a place,open a broser,play a youtube audio


text = gTTS("Hello guy's,how are you doing?")
#text.save("audio.mp3")
playsound.playsound("audio.mp3")
'''

#Import the libararies

from gtts import gTTS
import playsound
import time
import webbrowser    #it is default
import uuid        #It is default
import speech_recognition as sr
import os

#let uss create listen function

def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    #we will take micro phone as source
    with sr.Microphone() as source:
        print("Ika modeledadamma")
        audio = r.listen(source,phrase_time_limit=10)  #pharse_time_limit is adefault argument
    #we need to give our text as voice
    data = ""
    #here i will give exceptions(try,except)
    try:
        data = r.recognize_google(audio)
        print("You said: ",data)
        
    except sr.UnknowValueError as e:
        print("request Failed")

    except sr.RequestError as e:
        print("speak clearly request is failing")

    return data
    #tts=gTTS(data)
    #tts.dave("new.mp3")
    #playsound.playsound("new.mp3")

#listen()

def respond(String):
    """Function to respond back"""
    print(String)
    tts=gTTS(String)
    tts.save("speech.mp3")

    #we using uuid --.to randomize the content in the audio file
    filename="speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Here we will make our virtual assistant int action

def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening=True
        respond("I am fine thanks for asking")
        
    elif "what are you plans" in data:
        listening=True
        respond("Only Study..One focus in 2026")

    elif "How are things going" in data:
        listening=True
        respond("Anthaa Okay inka nene set avvali")

    elif "Time" in data:
        listening=True
        respond(time.ctime())

    elif"stop talking" in data:
        listening=False
        respond("Okay cool...kopadaku bye")

    try:
        return listening

    except UnboundLocalError as e:
        print(" Make Sure speak louder and Faster")

respond("Hey Lavanya...Good to hear from you.How are you?")

listening=True
while listening:
    data = listen()
    listening = va(data)
    
    
       























            
