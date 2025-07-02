# Mood-Based-Music-Generator

This project takes a sentence describing your mood and generates a unique MIDI music track to match that mood. It uses sentiment analysis with NLTK and the PrettyMIDI library to produce a melody reflecting the emotional tone of your input.

## 🧠 How It Works

1. **Sentiment Detection**: Your mood sentence is analyzed using VADER (Valence Aware Dictionary and sEntiment Reasoner).
2. **Mood Classification**: Based on sentiment score or keywords, your mood is classified (e.g., happy, sad, calm).
3. **Music Generation**: A short melody is generated using MIDI notes tailored to the mood, with tempo and instrument changes.

## Future Work

1. Support for More Emotions: Extend mood detection to include a wider range of emotional states like excitement, anxiety, or nostalgia.
2. User-Selectable Instruments: Allow users to choose instruments to personalize the generated music.
3. Longer and Structured Compositions: Generate more complex MIDI tracks with structured sections like intro, chorus, and outro.

## 🛠 Dependencies

- numpy
- pretty_midi
- nltk
- music21

Install dependencies using:

```bash
pip install -r requirements.txt
