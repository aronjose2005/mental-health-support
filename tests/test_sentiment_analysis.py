import pytest
from src.quantum_sentiment_analysis import analyze_sentiment

def test_analyze_sentiment():
    score = analyze_sentiment("I am very happy today")
    assert -1.0 <= score <= 1.0
