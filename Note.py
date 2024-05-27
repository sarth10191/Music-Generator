from utils import NOTE_MAP
from Tone import Tone, sine_x
import threading

class Note:
    def __init__(self, note_str, duration = 0.5):
        main_note = note_str[0]
        self.note_str = main_note +note_str[1:]
        self.duration = duration
        self.freq = NOTE_MAP[self.note_str]

    def play(self, speaker = None):
        Tone.sine(self.freq, duration=self.duration, speaker = speaker)

    @staticmethod
    def play_chord(notes_list):
        note_threads = []
 
        for note in notes_list:
            note_thread = threading.Thread(target=note.play)
            note_threads.append(note_thread)

        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()