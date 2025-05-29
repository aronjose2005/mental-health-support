import openai_whisper as whisper

# Audio-to-text for emotional input using Whisper
def audio_to_text(audio_path):
    try:
        model = whisper.load_model("small")
        result = model.transcribe(audio_path)
        return result["text"]
    except FileNotFoundError:
        return "Audio file not found. Please provide a valid audio file."
