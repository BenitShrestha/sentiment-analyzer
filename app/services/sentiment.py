from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Using the VADER library

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> dict:
    """Takes a string, returns a dictionary with results"""
    scores = analyzer.polarity_scores(text)

    sentiment = (
        "positive"
        if scores["compound"] > 0.05
        else ("negative" if scores["compound"] < -0.05 else "neutral")
    )

    return {"sentiment": sentiment, "scores": scores}
