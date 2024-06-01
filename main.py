from Note import Note
from Track import Track
from raga import Raga
from Structure1 import Gat

raga = Raga("ga", mode="manual", varjyaAaroha=["ni"], varjyaAvaroha=["ni"])
gat = Gat(raga, matras=8)

print(gat.track)
# notes_array = ['ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're', 'ga', 'pa', 're', 'ga', 'ma', 'pa', 'ma', 'pa', 'ga', 'ga', 'ma', 'pa', 'dha', 'sa', 'dha', 'pa', 'ma', 'ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're',
#                'ga', 'ma', 'ga', 'sa', 'sa', 'ga', 'ma', 'pa', 'dha', 'pa', 'dha', 'pa', 'ma', 'ga', 'sa', 'ma', 'ga', 'pa', 'pa', 'ma', 'ga', 'ga', 're', 'ga', 'ma', 'ga', 'ma', 'pa', 'dha', 'sa', 'dha', 'pa', 'ma', 'ma', 'pa', 'dha', 'ga', 'ma', 'ma', 'ga', 'dha', 'sa', 're', 'ga', 'ga', 're', 'sa', 're', 'ga']
notes_array = gat.track
# Create Note instances for each note in the array
notes_instances = []
for i in range(len(notes_array)):
    if notes_array[i] == "-":
        continue
    if notes_array[i+1!="-"]:
        notes_instances.append(Note(note_str=notes_array[i]))
    else:
        notes_instances.append(Note(note_str=notes_array[i],duration=1))
        
# notes_instances = [Note(note_str) for note_str in notes_array]

# Create a Track instance with the list of Note instances
track = Track(notes_instances)

# Play the track
track.play()
