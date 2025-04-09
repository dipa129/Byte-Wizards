import streamlit as st
import pandas as pd
from chat_analyzer import analyze_chat_logs
from voice_analyzer import analyze_voice_clip

st.set_page_config(page_title="ClassSentiment", layout="centered")
st.title("🎓 ClassSentiment: AI-Powered Classroom Analyzer")

# --- Chat Log Analyzer Section ---
st.header("📄 Analyze Chat Logs")
chat_input = st.text_area("Paste classroom chat logs (one message per line):", height=200)

if st.button("Analyze Chat Logs"):
    if chat_input.strip():
        chat_lines = chat_input.strip().split('\n')
        chat_df = analyze_chat_logs(chat_lines)
        st.dataframe(chat_df)
    else:
        st.warning("Please enter some chat logs.")

# --- Voice Clip Analyzer Section ---
st.header("🎙 Analyze Student Voice Clip")

uploaded_audio = st.file_uploader("Upload MP3 voice clip", type=['mp3'])

if uploaded_audio and st.button("Analyze Voice"):
    with open("temp_upload.mp3", "wb") as f:
        f.write(uploaded_audio.read())

    text, emotion, sentiment = analyze_voice_clip("temp_upload.mp3")
    
    st.success("Voice Analysis Complete!")
    st.write(f"**Transcript:** {text}")
    st.write(f"**Emotion:** {emotion}")
    st.write(f"**Classroom Sentiment:** {sentiment}")
