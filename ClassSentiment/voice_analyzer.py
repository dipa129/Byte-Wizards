import speech_recognition as sr
from pydub import AudioSegment
from transformers import pipeline
from utils import map_emotion_to_sentiment

# Load model
classifier = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

def convert_mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

def transcribe_audio(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "[Could not transcribe]"

def analyze_voice_clip(mp3_file):
    wav_file = "temp.wav"
    convert_mp3_to_wav(mp3_file, wav_file)
    text = transcribe_audio(wav_file)
    prediction = classifier(text)[0]
    emotion = prediction['label']
    sentiment = map_emotion_to_sentiment(emotion)
    return text, emotion, sentiment
