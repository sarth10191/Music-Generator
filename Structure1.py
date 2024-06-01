from raga import Raga
from phrases_gen import PhraseGenerator
import random

class Gat:
    def __init__(self, raga:Raga, matras=8):
        self.rag = raga
        self.myPhraseGenerator = PhraseGenerator(raga=self.rag)
        self.matras = matras

        # Generate the track on initialization
        self.track = self.generate_track()

    def samaGenerator(self, GrahaPhrases, SamaPhrases):
        selected_phrases = []
        for i, j in zip(GrahaPhrases, SamaPhrases):
            if len(i) + len(j) == self.matras:
                selected_phrases.append(i + j)
        return random.choice(selected_phrases)

    def postSamaGenerator(self, SarvaPhrases, NyasaPhrases):
        selected_phrases = []
        for i, j in zip(SarvaPhrases, NyasaPhrases):
            if len(i) + len(j) == self.matras:
                selected_phrases.append(i + j)
        return random.choice(selected_phrases)

    def asama(self, s2postsama, GrahaPhrases, SamaPhrases):
        g = [phrase for phrase in GrahaPhrases if phrase[0] == s2postsama[-1]]
        if g:
            g1 = random.choice(g)
        else:
            g1 = []

        j = [j1 for j1 in SamaPhrases if len(g1) + len(j1) == self.matras]
        if j:
            j1 = random.choice(j)
            return g1 + j1
        return self.samaGenerator(GrahaPhrases, SamaPhrases)

    def generate_track(self):
        s1samapart = self.samaGenerator(self.myPhraseGenerator.GrahaPhrases, self.myPhraseGenerator.SamaPhrases)
        s1postSama = self.postSamaGenerator(self.myPhraseGenerator.SarvaPhrases, self.myPhraseGenerator.NyasaPhrases)

        s2sama = self.samaGenerator(self.myPhraseGenerator.GrahaPhrases, self.myPhraseGenerator.SamaPhrases)
        s2postSama = self.postSamaGenerator(self.myPhraseGenerator.SarvaPhrases, self.myPhraseGenerator.NyasaPhrases)

        s = s1samapart + s1postSama + s2sama + s2postSama + s1samapart + s1postSama

        a1sama = self.asama(s2postSama, self.myPhraseGenerator.GrahaPhrases, self.myPhraseGenerator.SamaPhrases)
        a1postsama = self.postSamaGenerator(self.myPhraseGenerator.SarvaPhrases, self.myPhraseGenerator.NyasaPhrases)
        
        a2sama = self.samaGenerator(self.myPhraseGenerator.GrahaPhrases, self.myPhraseGenerator.SamaPhrases)
        a2postsama = self.postSamaGenerator(self.myPhraseGenerator.SarvaPhrases, self.myPhraseGenerator.NyasaPhrases)

        a = a1sama + a1postsama + a2sama + a2postsama + s1samapart + s1postSama
        
        return s + a

# Create an instance of the Gat class
raga = Raga("ga", mode="auto", varjyaAaroha=["ni"], varjyaAvaroha=["ni"])
gat = Gat(raga, matras=8)
print(gat.track)
