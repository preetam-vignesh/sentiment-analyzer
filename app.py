from flask import Flask, render_template, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Flask app
app = Flask(__name__)

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Sentiment analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Get sentiment score
    sentiment_scores = sia.polarity_scores(text)
    sentiment_score = sentiment_scores['compound']

    # Determine sentiment category
    if sentiment_score >= 0.05:
        sentiment = 'pos'
    elif sentiment_score <= -0.05:
        sentiment = 'neg'
    else:
        sentiment = 'neu'

    return jsonify({'sentiment': sentiment, 'score': sentiment_score})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
