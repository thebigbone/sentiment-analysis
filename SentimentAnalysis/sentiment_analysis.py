import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def sentiment_analyzer(text_to_analyse):
    url = f'https://api.nlp-api.com/v1/sentiment?text={text_to_analyse}&api_token={os.getenv("API_KEY")}'
    response = requests.get(url)

    formatted_response = json.loads(response.text)

    final_lables = []
    final_scores = []

    for i in range(3):
        label = formatted_response['data'][0][i]['label']
        score = formatted_response['data'][0][i]['score']
        final_lables.append(label)
        final_scores.append(score)

    high_score = max(final_scores)
    high_label = final_scores.index(high_score)

    return {'label': final_lables[high_label], 'score': high_score}


'''
    if response.status_code == 200:


        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

        return {'label': label, 'score': score}
    if response.status_code == 500:
        return {'label': 'None', 'score': 'None'}
'''
