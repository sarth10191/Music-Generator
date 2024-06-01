from raga import Raga
from phrases_gen import PhraseGenerator
from Note import Note
import random
rag = Raga("dha", mode="auto", varjyaAaroha=["re"], varjyaAvaroha=["re"])
myPhraseGenerator = PhraseGenerator(raga=rag)
# print("Enter the numer of matras in selected tala.(16 or 12): ")
print(len(myPhraseGenerator.phrases_all))
matras = 8
remaining_matras = matras
# Constrinction of sthayi
# sthayiGrahaPhrase = []
# sthayisamaPhrase = []
# for i,j in zip(myPhraseGenerator.GrahaPhrases,myPhraseGenerator.SamaPhrases):
#     if len(i)+len(j) == matras:
#         sthayiGrahaPhrase = i
#         sthayiSamaPhrase = j
# sthayiSarvaPhrase = []
# sthayiVinyasaPhrase = []
# for i,j in zip(myPhraseGenerator.SarvaPhrases,myPhraseGenerator.NyasaPhrases):
#     if len(i)+len(j) == matras:
#         sthayiSarvaPhrase = i
#         sthayiVinyasaPhrase = j


# Function like sama part generator and Nyasa part generator
def samaGenerator(GrahaPhrases, SamaPhrases):
    selected_phrases = []
    for i, j in zip(GrahaPhrases, SamaPhrases):
        if len(i)+len(j) == matras:
            selected_phrases.append(i+j)
    return random.choice(selected_phrases)

s1samapart = samaGenerator(myPhraseGenerator.GrahaPhrases,
                         myPhraseGenerator.SamaPhrases)
# print(s1samapart)


def postSamaGenerator(SarvaPhrases, NyasaPhrases):
    selected_phrases = []
    for i, j in zip(SarvaPhrases, NyasaPhrases):
        if len(i)+len(j) == matras:
            selected_phrases.append(i+j)
    return random.choice(selected_phrases)
s1postSama = postSamaGenerator(myPhraseGenerator.SarvaPhrases,myPhraseGenerator.NyasaPhrases)

s2sama = samaGenerator(myPhraseGenerator.GrahaPhrases,
                         myPhraseGenerator.SamaPhrases)
s2postSama = postSamaGenerator(myPhraseGenerator.SarvaPhrases,myPhraseGenerator.NyasaPhrases)
s = s1samapart+s1postSama+s2sama+s2postSama+s1samapart+s1postSama
# print(s)
a = []
def asama(s2postsama,GrahaPhrases,SamaPhrases):
    g = []
    for phrase in GrahaPhrases:
        if phrase[0] == s2postsama[-1]:
            g.append(phrase)
    if g!=[]:
        g1 = random.choice(g)
    j = []
    for j1 in SamaPhrases:
        if len(g1)+len(j1) == matras:
            j.append(j1)
    if j!=[]:
        j1 = random.choice(j)
        return g1+j1
    return samaGenerator(myPhraseGenerator.GrahaPhrases, myPhraseGenerator.SamaPhrases)

    
a1sama = asama(s2postSama,myPhraseGenerator.GrahaPhrases,myPhraseGenerator.SamaPhrases)
a1postsama = postSamaGenerator(myPhraseGenerator.SarvaPhrases,myPhraseGenerator.NyasaPhrases)
a2sama = samaGenerator(myPhraseGenerator.GrahaPhrases,
                         myPhraseGenerator.SamaPhrases)
a2postsama = postSamaGenerator(myPhraseGenerator.SarvaPhrases,myPhraseGenerator.NyasaPhrases)
a = a1sama+a1postsama+a2sama+a2postsama+s1samapart+s1postSama
track = s+a
print(track)

