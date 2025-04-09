# Import functions from modules
from chat_analyzer import analyze_chat_logs           # For chat text sentiment analysis
from voice_analyzer import analyze_voice_clip         # For audio sentiment analysis

# Sample list of chat messages from students
chat_logs = [
    "I don't get this topic.",
    "This is so boring!",
    "Wow! That was fun!",
    "Can you explain again?",
]

# Perform chat log analysis
print(" Chat Log Analysis:")
chat_df = analyze_chat_logs(chat_logs)   # Run emotion classifier on chat logs
print(chat_df)                           # Display results as a table

# Analyze a student's voice clip
print("\n Voice Clip Analysis:")
transcribed, emotion, sentiment = analyze_voice_clip("student_voice.mp3")  # Analyze voice
print(f"Transcript: {transcribed}")  # Print what was said in the clip
print(f"Emotion: {emotion}")         # Print detected emotion
print(f"Sentiment: {sentiment}")     # Print mapped classroom sentiment (e.g., Confused)

