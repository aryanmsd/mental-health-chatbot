from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/bert-base-go-emotion",
    return_all_scores=True
)

def detect_emotion(text):
    emotions = emotion_classifier(text)[0]
    top_emotion = max(emotions, key=lambda x: x["score"])
    return top_emotion["label"]
