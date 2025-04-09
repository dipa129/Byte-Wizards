from chat_analyzer import analyze_chat_logs
from voice_analyzer import analyze_voice_clip

# Sample chat logs
chat_logs = [
    "I don't get this topic.",
    "This is so boring!",
    "Wow! That was fun!",
    "Can you explain again?",
]

print("🧾 Chat Log Analysis:")
chat_df = analyze_chat_logs(chat_logs)
print(chat_df)

print("\n🎙 Voice Clip Analysis:")
transcribed, emotion, sentiment = analyze_voice_clip("student_voice.mp3")
print(f"Transcript: {transcribed}")
print(f"Emotion: {emotion}")
print(f"Sentiment: {sentiment}")
