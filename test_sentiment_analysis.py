from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer('I love python')
        self.assertEqual(result1['label'], 'positive')

        result2 = sentiment_analyzer('I hate python')
        self.assertEqual(result2['label'], 'negative')

        result3 = sentiment_analyzer('I am neutral with python')
        self.assertEqual(result3['label'], 'neutral')


if __name__ == '__main__':
    unittest.main()
