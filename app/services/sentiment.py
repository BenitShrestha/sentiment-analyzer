from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    sentiment = (
        "positive"
        if scores["compound"] > 0.05
        else "negative" if scores["compound"] < -0.05 else "neutral"
    )
    return {"sentiment": sentiment, "scores": scores}
