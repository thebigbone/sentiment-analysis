from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer", methods=['GET'])
def sent_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyse)

    label = response['label']
    score = response['score']

    return f'text is <b>{label}<b> with score of <b>{score}</b>'


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
