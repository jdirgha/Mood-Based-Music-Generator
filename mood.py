import numpy as np
import pretty_midi
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random
import os

try:
    from IPython.display import Audio, display
except ImportError:
    Audio = None

# Download NLTK lexicon
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_mood(sentence):
    sentiment_score = sia.polarity_scores(sentence)
    sentence = sentence.lower()

    if "happy" in sentence or "joyful" in sentence or "cheerful" in sentence or sentiment_score['compound'] > 0.5:
        return "happy"
    elif "sad" in sentence or "depressed" in sentence or "down" in sentence or sentiment_score['compound'] < -0.5:
        return "sad"
    elif "relaxed" in sentence or "peaceful" in sentence or "calm" in sentence:
        return "calm"
    elif "excited" in sentence or "energetic" in sentence:
        return "energetic"
    elif "classical" in sentence:
        return "classical"
    elif "hip-hop" in sentence or "rap" in sentence:
        return "hip-hop"
    elif "jazz" in sentence:
        return "jazz"
    elif "pop" in sentence:
        return "pop"
    else:
        return "calm"

def generate_music(mood):
    mood_settings = {
        "happy": {"tempo": 140, "scale": [60, 62, 64, 65, 67, 69, 71, 72], "instrument": 1},
        "sad": {"tempo": 60, "scale": [60, 62, 63, 65, 67, 68, 70, 72], "instrument": 40},
        "calm": {"tempo": 80, "scale": [60, 62, 64, 66, 68, 70, 72, 74], "instrument": 74},
        "energetic": {"tempo": 160, "scale": [60, 64, 67, 71, 72, 76, 79, 83], "instrument": 30},
        "classical": {"tempo": 100, "scale": [60, 62, 64, 65, 67, 69, 71, 72], "instrument": 24},
        "hip-hop": {"tempo": 90, "scale": [36, 38, 40, 42, 44, 46, 48], "instrument": 117},
        "jazz": {"tempo": 120, "scale": [60, 62, 63, 65, 67, 69, 70, 72], "instrument": 33},
        "pop": {"tempo": 128, "scale": [60, 62, 64, 65, 67, 69, 71, 74], "instrument": 5},
    }

    settings = mood_settings.get(mood, mood_settings["calm"])

    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=settings["instrument"])

    time = 0
    for _ in range(16):
        note_pitch = random.choice(settings["scale"])
        note_length = random.choice([0.25, 0.5, 1.0, 1.5])
        note_velocity = random.randint(80, 120)

        note = pretty_midi.Note(
            velocity=note_velocity,
            pitch=note_pitch,
            start=time,
            end=time + note_length
        )
        instrument.notes.append(note)
        time += note_length

    midi.instruments.append(instrument)
    midi.write("generated_music.mid")
    print(f"🎶 Music generated based on mood: {mood}")

def play_midi():
    if os.path.exists("generated_music.mid") and Audio:
        print("Playing the generated music...")
        display(Audio("generated_music.mid", rate=16000))
    else:
        print("Playback not supported or file not found.")

if __name__ == "__main__":
    user_input = input("Describe your mood: ")
    mood = analyze_mood(user_input)
    print(f"🧠 Detected Mood: {mood}")
    generate_music(mood)
    play_midi()
