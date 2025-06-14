# Save this as train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset
data = {
    'text': ['I love this product', 'This is the worst thing ever', 'Absolutely fantastic', 'Not good', 'I hate this', 'Very nice and useful', 'Terrible experience', 'Best I ever used'],
    'label': ['pos', 'neg', 'pos', 'neg', 'neg', 'pos', 'neg', 'pos']
}

df = pd.DataFrame(data)

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open('sentiment_model.pkl', 'wb') as file:
    pickle.dump((model, vectorizer), file)

print("Model trained and saved successfully.")
