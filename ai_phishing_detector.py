from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training dataset (simple demo dataset)
emails = [
    "verify your account immediately",
    "click here to reset your password",
    "urgent login required",
    "meeting schedule for tomorrow",
    "project update attached",
    "team lunch invitation"
]

labels = [
    1,  # phishing
    1,
    1,
    0,  # safe
    0,
    0
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

model = LogisticRegression()
model.fit(X, labels)


def predict_email(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    if prediction == 1:
        return "PHISHING"
    else:
        return "SAFE"
