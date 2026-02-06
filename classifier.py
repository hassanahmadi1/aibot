import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def classify_text(text):
    x = vectorizer.transform([text])
    pred = model.predict(x)[0]
    prob = model.predict_proba(x).max()
    return pred, prob