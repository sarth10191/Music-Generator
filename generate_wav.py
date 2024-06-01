import numpy as np
import scipy.io.wavfile as wavfile
from utils import NOTE_MAP
from main import notes_array

default_duration = 0.5  # Default duration of each note

# Sample rate (samples per second)
sample_rate = 44100

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # 0.5 to adjust amplitude
    return wave

def notes_to_wav(note_sequence, filename):
    audio_sequence = np.array([], dtype=np.float32)

    for i in range(len(note_sequence)-1):
        if note_sequence[i] == "-":
            continue
        if note_sequence[i+1]!="-":
            frequency = NOTE_MAP.get(note_sequence[i], 0)
            if frequency > 0:
                wave = generate_sine_wave(frequency, default_duration, sample_rate)
                audio_sequence = np.concatenate((audio_sequence, wave))
            else:
                silence = np.zeros(int(sample_rate * default_duration))
                audio_sequence = np.concatenate((audio_sequence, silence))
        elif note_sequence[i+1] =="-":
            frequency = NOTE_MAP.get(note_sequence[i], 0)
            if frequency > 0:
                wave = generate_sine_wave(frequency, default_duration*2, sample_rate)
                audio_sequence = np.concatenate((audio_sequence, wave))
            else:
                silence = np.zeros(int(sample_rate * (default_duration*2)))
                audio_sequence = np.concatenate((audio_sequence, silence))


    audio_sequence = np.int16(audio_sequence / np.max(np.abs(audio_sequence)) * 32767)

    wavfile.write(filename, sample_rate, audio_sequence)

note_sequence = notes_array

# Generate WAV file from the note sequence
notes_to_wav(note_sequence, 'output.wav')

print("WAV file generated successfully!")
