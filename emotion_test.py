from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="bhadresh-savani/bert-base-go-emotion",
    return_all_scores=True
)

print(clf("I feel anxious about my future"))
