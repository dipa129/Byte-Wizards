

def map_emotion_to_sentiment(label):
    label = label.lower()
    if label in ['confusion', 'sadness', 'fear']:
        return 'Confused'
    elif label in ['joy', 'love', 'surprise']:
        return 'Engaged'
    elif label in ['anger', 'disgust']:
        return 'Bored'
    else:
        return 'Neutral'
