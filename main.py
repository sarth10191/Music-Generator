from Note import Note
from Track import Track
# from raga import Raga
# from structure import Bandish


notes_array = ['ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're', 'ga', 'pa', 're', 'ga', 'ma', 'pa', 'ma', 'pa', 'ga', 'ga', 'ma', 'pa', 'dha', 'sa', 'dha', 'pa', 'ma', 'ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're',
               'ga', 'ma', 'ga', 'sa', 'sa', 'ga', 'ma', 'pa', 'dha', 'pa', 'dha', 'pa', 'ma', 'ga', 'sa', 'ma', 'ga', 'pa', 'pa', 'ma', 'ga', 'ga', 're', 'ga', 'ma', 'ga', 'ma', 'pa', 'dha', 'sa', 'dha', 'pa', 'ma', 'ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're', 'ga']
# notes_array = track
# Create Note instances for each note in the array
notes_instances = [Note(note_str) for note_str in notes_array]

# Create a Track instance with the list of Note instances
track = Track(notes_instances)

# Play the track
track.play()
