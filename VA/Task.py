# Import libraries
from gtts import gTTS
import os
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import random
import segno

# Listen function for speech recognition
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    # Take microphone as the input source
    with sr.Microphone() as source:
        print("Ika Modaledadhamaa..")
        audio = r.listen(source, phrase_time_limit=10)
    # Convert voice into text
    data = ""
    # Handle speech recognition exceptions
    try:
        data = r.recognize_google(audio)
        print("You said:", data)
    except sr.UnknownValueError:
        print("Request Failed")
    except sr.RequestError:
        print("Speak clearly, request is failing")
    return data

# Respond function for voice output
def respond(String):
    """Function to respond back"""
    print(String)
    # Convert text into speech
    tts = gTTS(String)
    # Create a unique audio file name
    filename = "Speech%s.mp3" % str(uuid.uuid4())
    # Save speech as MP3
    tts.save(filename)
    # Play the audio
    playsound.playsound(filename)
    # Delete the temporary audio file
    os.remove(filename)

# Developer QR code function
def generate_developer_qr():
    """Generate Developer Profile QR Code"""
    # Developer profile information
    profile = """
================================
        DEVELOPER PROFILE
================================
Name: Lavanya Yalamanchi
Role: Python Full Stack Developer
Skills:
Python
Java
C
SQL
HTML
CSS
JavaScript
React
Pandas
NumPy
Power BI

Email:
lavanyayalamanchi2005@gmail.com

LinkedIn:
https://www.linkedin.com/in/lavanya-yalamanchi/

GitHub:
https://github.com/YalamanchiLavanya
================================
        THANK YOU!
================================
"""
    # Create QR code
    qr = segno.make(profile)
    # Save QR code as image
    qr.save("developer_profile.png", scale=10)
    print("Developer Profile QR Code Created Successfully!")

# Virtual Assistant function
def va(data):
    """Virtual Assistant with different actions"""
    # Convert voice command to lowercase
    data = data.lower()
    listening = True
    # Check how are you command
    if "how are you" in data:
        respond("I'm fine, thanks for asking.")
    # Check plans command
    elif "what are your plans" in data:
        respond("My focus is learning Python, Data Science and Full Stack Development.")
    # Check how things are going
    elif "how are things going" in data:
        respond("Everything is going well.")
    # Tell current time
    elif "time" in data:
        respond(time.ctime())
    # Open Google
    elif "open google" in data:
        respond("Opening Google")
        webbrowser.open("https://www.google.com")
    # Open YouTube
    elif "open youtube" in data:
        respond("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    # Open WhatsApp
    elif "open whatsapp" in data:
        respond("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    # Open Google Maps
    elif "open maps" in data:
        respond("Opening Maps")
        webbrowser.open("https://maps.google.com")
    # Locate a place
    elif "locate" in data:
        location = data.replace("locate", "").strip()
        respond("Locating " + location)
        webbrowser.open("https://www.google.com/maps/search/" + location)
        print("Located")
    # Developer QR code option
    elif "qr" in data:
        respond("Okay, generating your developer profile QR code.")
        generate_developer_qr()
        respond("Developer profile QR code has been generated successfully.")
        # Open QR image automatically
        os.startfile("developer_profile.png")
    # Number guessing game
    elif "number game" in data:
        respond("Okay, let's play a number guessing game. I have selected a number between 1 and 20.")
        # Generate random number
        number = random.randint(1, 20)
        # Give the user 3 chances
        for i in range(3):
            respond("Guess the number")
            # Listen to user's guess
            guess_data = listen()
            try:
                # Convert voice input into integer
                guess = int(guess_data)
                # Check correct guess
                if guess == number:
                    respond("Congratulations! You guessed the correct number.")
                    break
                # Check if guess is low
                elif guess < number:
                    respond("Your guess is too low. Try again.")
                # Check if guess is high
                else:
                    respond("Your guess is too high. Try again.")
            except ValueError:
                respond("Please say a valid number.")
        # If all three attempts are completed
        else:
            respond("Sorry, you lost the game. The number was " + str(number))
    # Stop the assistant
    elif "stop talking" in data or "stop" in data:
        listening = False
        respond("Okay, bye Lavanya. Have a great day!")
    # Unknown command
    else:
        print("Command not recognized.")
    return listening

# Start the Virtual Assistant
respond("Hey Lavanya. Good to hear from you. How are you?")
listening = True

# Continuously listen for commands
while listening:
    data = listen()
    listening = va(data)
