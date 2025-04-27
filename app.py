import os
import speech_recognition as sr
import pyttsx3
from flask import Flask, render_template, request, jsonify
from skills import time_skill, weather_skill, calculator, email, ai_chat
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

class Assistant:
    def __init__(self):
        self.name = "Jarvis"
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.setup_voice()
        
    def setup_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Female voice
        self.engine.setProperty('rate', 150)  # Speaking speed
        
    def speak(self, text):
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"You: {command}")
            return command
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
    
    def process_command(self, command):
        if not command:
            return "Sorry, I didn't catch that."
            
        if "time" in command:
            return time_skill.get_time()
        elif "date" in command:
            return time_skill.get_date()
        elif "weather" in command:
            location = command.split("weather in ")[1] if "weather in" in command else None
            return weather_skill.get_weather(location)
        elif "calculate" in command:
            return calculator.calculate(command.replace("calculate", ""))
        elif "email" in command:
            return "Please use the web interface to send emails"
        elif any(word in command for word in ["hi", "hello", "hey"]):
            return f"Hello! I'm {self.name}, your personal assistant."
        elif any(word in command for word in ["exit", "bye", "goodbye"]):
            return "Goodbye! Have a nice day."
        else:
            return ai_chat.chat_with_ai(command)

assistant = Assistant()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    command = data['message'].lower()
    response = assistant.process_command(command)
    return jsonify({'response': response})

@app.route('/api/voice', methods=['POST'])
def voice():
    command = assistant.listen()
    if command:
        response = assistant.process_command(command)
        return jsonify({'response': response})
    return jsonify({'response': "Sorry, I didn't catch that."})

if __name__ == '__main__':
    app.run(debug=True)