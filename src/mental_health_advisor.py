from transformers import pipeline

# Generate mental health advice using Llama (simulated with OPT-350m)
def generate_mental_health_advice(user_input, sentiment_score):
    generator = pipeline("text-generation", model="facebook/opt-350m")  # Llama placeholder
    prompt = f"Provide ethical mental health advice for: {user_input} (Sentiment Score: {sentiment_score})"
    advice = generator(prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]
    return advice
