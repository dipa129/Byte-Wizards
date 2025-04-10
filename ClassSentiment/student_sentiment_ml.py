import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

st.set_page_config(page_title="Student Sentiment ML", layout="centered")
st.title("Student Sentiment Analyzer (ML + Streamlit)")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file with 'text' and 'label' columns", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if 'text' in df.columns and 'label' in df.columns:
        st.subheader("Dataset Preview")
        st.write(df.head())

        # Train ML Model
        X = df['text']
        y = df['label']
        vectorizer = TfidfVectorizer()
        X_vec = vectorizer.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)

        st.success(f"Model trained with accuracy: {score:.2f}")

        # Live prediction
        st.subheader("Test It Out")
        user_input = st.text_input("Enter a student message to analyze:")

        if user_input:
            user_vec = vectorizer.transform([user_input])
            prediction = model.predict(user_vec)[0]
            st.write(f"**Predicted Sentiment**: {prediction}")

        # Show classification report
        if st.checkbox("Show detailed classification report"):
            y_pred = model.predict(X_test)
            st.text(classification_report(y_test, y_pred))
    else:
        st.error("CSV must have 'text' and 'label' columns.")
