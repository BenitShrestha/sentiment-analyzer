from app.services.sentiment import analyze_sentiment


def test_positive_statement():
    text = "I am delighted with the dish!"
    result = analyze_sentiment(text)
    assert result["sentiment"] == "positive"


def test_negative_sentiment():
    text = "This is depressing, my dog died!"
    result = analyze_sentiment(text)
    assert result["sentiment"] == "negative"


def test_neutral_sentiment():
    text = "I ate an apple!"
    result = analyze_sentiment(text)
    assert result["sentiment"] == "neutral"
