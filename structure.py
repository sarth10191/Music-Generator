import random
from raga import Raga
from phrases_gen import PhraseGenerator
from Note import Note

class Bandish:
    def __init__(self, raga, matras):
        self.raga = raga
        self.matras = matras
        self.phrase_generator = PhraseGenerator(raga=self.raga)

    def sama_generator(self, GrahaPhrases, SamaPhrases):
        selected_phrases = []
        for i, j in zip(GrahaPhrases, SamaPhrases):
            if len(i) + len(j) == self.matras:
                selected_phrases.append(i + j)
        if selected_phrases:
            return random.choice(selected_phrases)
        else:
            raise ValueError("No matching Sama phrases found.")

    def post_sama_generator(self, SarvaPhrases, NyasaPhrases):
        selected_phrases = []
        for i, j in zip(SarvaPhrases, NyasaPhrases):
            if len(i) + len(j) == self.matras:
                selected_phrases.append(i + j)
        if selected_phrases:
            return random.choice(selected_phrases)
        else:
            raise ValueError("No matching Nyasa phrases found.")

    def asama(self, s2postsama, GrahaPhrases, SamaPhrases):
        g = [phrase for phrase in GrahaPhrases if phrase[0] == s2postsama[-1]]
        if not g:
            raise ValueError("No matching Graha phrases found.")
        
        g1 = random.choice(g)
        j = [j1 for j1 in SamaPhrases if len(g1) + len(j1) == self.matras]
        if not j:
            raise ValueError("No matching Sama phrases found.")
        
        j1 = random.choice(j)
        return g1 + j1

    def generate_track(self):
        s1samapart = self.sama_generator(self.phrase_generator.GrahaPhrases,
                                         self.phrase_generator.SamaPhrases)
        s1postSama = self.post_sama_generator(self.phrase_generator.SarvaPhrases,
                                              self.phrase_generator.NyasaPhrases)

        s2sama = self.sama_generator(self.phrase_generator.GrahaPhrases,
                                     self.phrase_generator.SamaPhrases)
        s2postSama = self.post_sama_generator(self.phrase_generator.SarvaPhrases,
                                              self.phrase_generator.NyasaPhrases)

        s = s1samapart + s1postSama + s2sama + s2postSama + s1samapart + s1postSama

        a1sama = self.asama(s2postSama, self.phrase_generator.GrahaPhrases,
                            self.phrase_generator.SamaPhrases)
        a1postSama = self.post_sama_generator(self.phrase_generator.SarvaPhrases,
                                              self.phrase_generator.NyasaPhrases)
        a2sama = self.sama_generator(self.phrase_generator.GrahaPhrases,
                                     self.phrase_generator.SamaPhrases)
        a2postSama = self.post_sama_generator(self.phrase_generator.SarvaPhrases,
                                              self.phrase_generator.NyasaPhrases)
        a = a1sama + a1postSama + a2sama + a2postSama + s1samapart + s1postSama

        track = s + a
        return track

# Example usage:
rag = Raga("ga", mode="auto", varjyaAaroha=["ni"], varjyaAvaroha=["ni"])
bandish = Bandish(raga=rag, matras=8)
track = bandish.generate_track()
print(track)

# Convert the track to Note objects if necessary
# track_notes = [Note(note) for note in track]
# print(track_notes)
