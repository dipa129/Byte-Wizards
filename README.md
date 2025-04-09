# Byte-Wizards



# 🎓 Student Engagement Analyzer

An AI-powered tool that detects emotions and engagement levels in students using their **voice recordings** and **chat logs**. This helps educators and learning platforms understand how students feel during online classes or self-paced learning. 📚🧠🎙️

---

## 📌 Overview

The **Student Engagement Analyzer** is a Python-based project that uses:

- 🎙 **Voice Transcription** to convert speech to text  
- 🤖 **Emotion Detection** via Hugging Face Transformers  
- 🧠 **Sentiment Mapping** to label students as Confused, Engaged, or Bored  
- 🧾 **Chat Log Analysis** for text-based engagement detection  

---

## 🎯 Concept

The idea is simple but powerful:

> Let’s analyze what students say (via voice or chat) ➡ understand how they feel (emotion) ➡ decide how engaged they are (sentiment).

This project can be used to:
- Monitor student moods during e-learning sessions.
- Identify when students are confused or bored.
- Help teachers adapt content or delivery methods.

---

## ⚙️ How It Works

### 🔹 Chat Log Analysis
1. Accepts a list of student messages.
2. Each message is analyzed using a transformer-based emotion classifier.
3. Emotions like *joy*, *sadness*, *confusion*, *anger* are detected.
4. These are mapped to simplified engagement sentiments like *Engaged*, *Confused*, *Bored*.

### 🔹 Voice Clip Analysis
1. Accepts an `.mp3` voice recording.
2. Converts it to `.wav` using **pydub**.
3. Transcribes audio to text using **SpeechRecognition** + Google Speech API.
4. Transcribed text is passed through the emotion classifier.
5. The detected emotion is mapped to engagement sentiment.

---

## 🧱 Folder Structure

```bash
student-engagement-analyzer/
│
├── main.py                 # Entry point: analyzes both chat and voice
├── chat_analyzer.py        # Handles chat log emotion analysis
├── voice_analyzer.py       # Handles voice transcription and emotion analysis
├── utils.py                # Contains emotion-to-sentiment mapping
├── requirements.txt        # Project dependencies
├── student_voice.mp3       # Sample student voice file
└── README.md               # Project documentation (this file)

# 📂Example Output

🧾 Chat Log Analysis:
+-------------------------+-----------+------------+
| Text                   | Emotion   | Sentiment  |
+-------------------------+-----------+------------+
| I don't get this topic.| Confusion | Confused   |
| This is so boring!     | Anger     | Bored      |
| Wow! That was fun!     | Joy       | Engaged    |
| Can you explain again? | Confusion | Confused   |

🎙 Voice Clip Analysis:
Transcript: I really enjoyed that session!
Emotion: Joy
Sentiment: Engaged
