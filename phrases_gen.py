from itertools import product
from raga import Raga
from LML import LML

class PhraseGenerator:
    def __init__(self, raga: Raga):
        self.raga = raga
        self.Aarohi_seq, self.Avarohi_seq = self.seq_phrases()
        self.mixedAA = self.fresequencial_AA()
        self.mixedDD = self.fresequencial_DD()
        self.mixedAD = self.fresequencial_AD()
        self.mixedDA = self.fresequencial_DA()
        self.meendAA = self.freemeend_AA()
        self.meendAV = self.freemeend_AV()
        self.ALM_all = self.ALM()
        self.phrases_all = self.all_phrases()
        self.GrahaPhrases = []
        self.NyasaPhrases = []
        self.SamaPhrases = []
        self.AmsaPhrases = []
        self.VadiPhrases = []
        self.SamvadiPhrases = []
        self.AnuvadiPhrases = []
        self.AnuanuvadiPhrases = []
        self.SarvaPhrases = []
        self.EmotivePhrases = []
        self.BhavaPhrases = []
        self.sort()



    def seq_phrases(self):
        """Function to create phrases of sequential elements from aaroha and avaroha of the raga"""
        Aarohi_seq = []
        Avarohi_seq = []
        for i in range(1, 5):
            for j in range(len(self.raga.aaroha) - i + 1):
                Aarohi_seq.append(self.raga.aaroha[j:i + j])
        for i in range(1, 5):
            for j in range(len(self.raga.avaroha) - i + 1):
                Avarohi_seq.append(self.raga.avaroha[j:i + j])
        return Aarohi_seq, Avarohi_seq

    def fresequencial_AA(self):
        mixedAA = []
        for p1, p2 in product(self.Aarohi_seq, self.Aarohi_seq):
            if self.raga.aaroha.index(p1[-1]) == self.raga.aaroha.index(p2[0]) - 1:
                if p1 + p2 not in mixedAA:
                    mixedAA.append(p1 + p2)
        return mixedAA

    def fresequencial_DD(self):
        mixedDD = []
        for p1, p2 in product(self.Avarohi_seq, self.Avarohi_seq):
            if self.raga.avaroha.index(p1[-1]) == self.raga.avaroha.index(p2[0]) - 1:
                if p1 + p2 not in mixedDD:
                    mixedDD.append(p1 + p2)
        return mixedDD

    def fresequencial_AD(self):
        mixedAD = []
        for p1, p2 in product(self.Aarohi_seq, self.Avarohi_seq):
            if self.raga.aaroha.index(p1[-1]) == self.raga.aaroha.index(p2[0]) + 1:
                if p1 + p2 not in mixedAD:
                    mixedAD.append(p1 + p2)
        return mixedAD

    def fresequencial_DA(self):
        mixedDA = []
        for p1, p2 in product(self.Avarohi_seq, self.Aarohi_seq):
            if self.raga.aaroha.index(p1[-1]) == self.raga.aaroha.index(p2[0]) - 1:
                if p1 + p2 not in mixedDA:
                    mixedDA.append(p1 + p2)
        return mixedDA

    def freemeend_AA(self):
        lml = LML()
        meendAA = []
        for p1, p2 in product(self.Aarohi_seq, self.Aarohi_seq):
            if p2[0] in lml.sga(s1=p1[-1]):
                if p1 + p2 not in meendAA:
                    meendAA.append(p1 + p2)
            if p2[0] in lml.skga(s1=p1[-1]):
                if p1 + p2 not in meendAA:
                    meendAA.append(p1 + p2)
            if p2[0] in lml.spa(s1=p1[-1]):
                if p1 + p2 not in meendAA:
                    meendAA.append(p1 + p2)
            if p2[0] in lml.sma(s1=p1[-1]):
                if p1 + p2 not in meendAA:
                    meendAA.append(p1 + p2)
        return meendAA

    def freemeend_AV(self):
        lml = LML()
        meendAV = []
        for p1, p2 in product(self.Avarohi_seq, self.Avarohi_seq):
            if p1[0] in lml.sga(s1=p2[-1]):
                if p1 + p2 not in meendAV:
                    meendAV.append(p1 + p2)
            if p1[0] in lml.skga(s1=p2[-1]):
                if p1 + p2 not in meendAV:
                    meendAV.append(p1 + p2)
            if p1[0] in lml.spa(s1=p2[-1]):
                if p1 + p2 not in meendAV:
                    meendAV.append(p1 + p2)
            if p1[0] in lml.sma(s1=p2[-1]):
                if p1 + p2 not in meendAV:
                    meendAV.append(p1 + p2)
        return meendAV

    def ALM(self):
        ALM = []
        for i in self.raga.aaroha:
            ALM.append([i, i])
            ALM.append([i, i, i])
        for i in range(len(self.raga.aaroha) - 1):
            ALM.append([self.raga.aaroha[i], self.raga.aaroha[i + 1]])
            ALM.append([self.raga.aaroha[i], self.raga.aaroha[i + 1], self.raga.aaroha[i], self.raga.aaroha[i + 1]])
            ALM.append([self.raga.aaroha[i], self.raga.aaroha[i + 1], self.raga.aaroha[i]])
        for i in range(len(self.raga.aaroha) - 4):
            ALM.append([self.raga.aaroha[i], self.raga.aaroha[i + 3], self.raga.aaroha[i + 2], self.raga.aaroha[i + 1]])
        return ALM

    def all_phrases(self):
        phrases = []
        for phrase_set in [self.ALM_all, self.meendAA, self.meendAV, self.mixedDA, self.mixedAA, self.mixedAD, self.mixedDD]:
            for phrase in phrase_set:
                if phrase not in phrases:
                    phrases.append(phrase)
        return phrases

    def sort(self):
        for phrase in self.phrases_all:
            if phrase[0] in self.raga.graha:
                self.GrahaPhrases.append(phrase)
            if phrase[0] in self.raga.nyasa:
                self.NyasaPhrases.append(phrase)
            if phrase[0] in self.raga.sama:
                self.SamaPhrases.append(phrase)
            if phrase[0] in self.raga.amsa:
                self.AmsaPhrases.append(phrase)
            if self.raga.vadi in phrase:
                self.VadiPhrases.append(phrase)
                # print(phrase)
            if self.raga.psamvadi in phrase:
                self.SamvadiPhrases.append(phrase)
            if self.raga.ssamvadi in phrase and phrase not in self.SamvadiPhrases:
                self.SamvadiPhrases.append(phrase)
            for i in self.raga.anuvadi:
                if i in phrase and phrase not in self.AnuvadiPhrases:
                    self.AnuvadiPhrases.append(phrase)
            for i in self.raga.anuanuvadi:
                if i in phrase and phrase not in self.AnuanuvadiPhrases:
                    self.AnuanuvadiPhrases.append(phrase)
                    self.SarvaPhrases.append(phrase)
            for i in self.raga.emotive:
                if i in phrase and phrase not in self.EmotivePhrases:
                    self.EmotivePhrases.append(phrase)
                    self.BhavaPhrases.append(phrase)
        for i in self.AnuvadiPhrases:
            if i not in self.BhavaPhrases:
                self.BhavaPhrases.append(i)
            if i not in self.SarvaPhrases:
                self.SarvaPhrases.append(i)
        
            
            
        

    
# Usage example
# raga = Raga(vadi="sa", mode="auto", varjyaAaroha=[], varjyaAvaroha=[])  # for testing purposes only
# lml = LML()  # for testing purposes only
# phrase_generator = PhraseGenerator(raga)
# phrases_all = phrase_generator.phrases_all
# print(len(phrases_all))
# for phrase in phrases_all:
#     print(phrase)
#
