# Mood-Based-Music-Generator

This project takes a sentence describing your mood and generates a unique MIDI music track to match that mood. It uses sentiment analysis with NLTK and the PrettyMIDI library to produce a melody reflecting the emotional tone of your input.

## 🧠 How It Works

1. **Sentiment Detection**: Your mood sentence is analyzed using VADER (Valence Aware Dictionary and sEntiment Reasoner).
2. **Mood Classification**: Based on sentiment score or keywords, your mood is classified (e.g., happy, sad, calm).
3. **Music Generation**: A short melody is generated using MIDI notes tailored to the mood, with tempo and instrument changes.

## 🛠 Dependencies

- numpy
- pretty_midi
- nltk
- music21

Install dependencies using:

```bash
pip install -r requirements.txt
