document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('analyzeBtn').addEventListener('click', analyzeSentiment);
    document.getElementById('toggleDarkModeBtn').addEventListener('click', toggleDarkMode);
    document.getElementById('clearHistoryBtn').addEventListener('click', clearHistory);
});

function analyzeSentiment() {
    const text = document.getElementById('textInput').value;

    if (text.trim() === '') {
        alert('Please enter some text!');
        return;
    }

    document.getElementById('spinner').style.display = 'block';

    fetch('https://sentiment-analyzer-je75.onrender.com/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('spinner').style.display = 'none';

        if (data.error) {
            document.getElementById('result').innerText = 'Error: ' + data.error;
        } else {
            let color = '';
            let sentimentText = '';
            let emoji = '';

            if (data.sentiment === 'Positive') {
                color = 'green';
                sentimentText = 'Positive';
                emoji = '😊';
            } else if (data.sentiment === 'Negative') {
                color = 'red';
                sentimentText = 'Negative';
                emoji = '😞';
            } else {
                color = 'gray';
                sentimentText = 'Neutral';
                emoji = '😐';
            }

            document.getElementById('result').innerHTML = `
                <span style="color:${color};">${emoji} ${sentimentText} (Score: ${data.score.toFixed(2)})</span>
            `;

            addToHistory(text, sentimentText, emoji);
        }
    })
    .catch(error => {
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('result').innerText = 'Error analyzing sentiment';
        console.error('Error:', error);
    });
}

function addToHistory(text, sentiment, emoji) {
    const historyList = document.getElementById('historyList');
    const listItem = document.createElement('li');
    listItem.textContent = `${emoji} "${text}" → ${sentiment}`;
    historyList.prepend(listItem);
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');

    const toggleButton = document.getElementById('toggleDarkModeBtn');
    if (document.body.classList.contains('dark-mode')) {
        toggleButton.textContent = 'Toggle Light Mode';
    } else {
        toggleButton.textContent = 'Toggle Dark Mode';
    }
}

function clearHistory() {
    document.getElementById('historyList').innerHTML = '';
}
