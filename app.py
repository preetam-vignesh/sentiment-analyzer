import os
from flask import Flask, render_template, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return jsonify({'sentiment': sentiment, 'score': sentiment_score})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render needs this
    app.run(host='0.0.0.0', port=port)
