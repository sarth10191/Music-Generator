raga = Raga(vadi="sa", mode="auto", varjyaAaroha=[], varjyaAvaroha=[])  # for testing purposes only
lml = LML()  # for testing purposes only
phrase_generator = PhraseGenerator(raga)
phrases_all = phrase_generator.phrases_all
print(len(phrases_all))
for phrase in phrases_all:
    print(phrase)