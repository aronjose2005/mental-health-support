import pytest
from src.mental_health_advisor import generate_mental_health_advice

def test_generate_mental_health_advice():
    advice = generate_mental_health_advice("I feel stressed", sentiment_score=0.5)
    assert isinstance(advice, str)
    assert len(advice) > 0
