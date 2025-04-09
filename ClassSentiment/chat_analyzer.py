# Import required libraries
import speech_recognition as sr  # For speech-to-text conversion
from pydub import AudioSegment   # For audio format conversion
from transformers import pipeline  # For loading the emotion classifier
from utils import map_emotion_to_sentiment  # Custom function to map emotion → sentiment

# Load a pre-trained HuggingFace model for emotion detection
classifier = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

def convert_mp3_to_wav(mp3_path, wav_path):
    """
    Converts an MP3 file to WAV format using pydub.
    Required because the speech recognition library needs WAV input.
    """
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

def transcribe_audio(wav_path):
    """
    Transcribes a WAV audio file into text using Google Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)  # Record the whole audio
        try:
            return recognizer.recognize_google(audio)
        except:
            return "[Could not transcribe]"

def analyze_voice_clip(mp3_file):
    """
    Main function to analyze a voice clip:
    - Convert MP3 to WAV
    - Transcribe speech to text
    - Use a Transformer model to detect emotion
    - Map emotion to classroom sentiment (Confused, Bored, Engaged)
    """
    wav_file = "temp.wav"
    convert_mp3_to_wav(mp3_file, wav_file)
    text = transcribe_audio(wav_file)
    prediction = classifier(text)[0]
    emotion = prediction['label']
    sentiment = map_emotion_to_sentiment(emotion)
    return text, emotion, sentiment

