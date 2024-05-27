from raga import Raga
from LML import LML
from itertools import product

raga = Raga(vadi="sa", mode="auto",varjyaAaroha=[],varjyaAvaroha=[])#for testing purposes only
lml = LML()#ftpo

# aaroha = raga.aaroha#ftpo
# avaroha = raga.avaroha#ftpo
##functions to select ghraha swars and nyasa swars and sama swars.
##for each phrase write a function to generate phrases.
##write a function to generate sthayi which calls two helper fuctions that have sthai structure and 
####selet appropriate phrases from the all generated phrases equried for each line.
##Similar functions for antara.
##Join sthayi and antara to form a bandish
##Create a track to export bandish as list.

def seq_phrases(raga: Raga)->list:
    """Function to create phrases of sequencial elements from aaroha and avaroha of the raag"""
    Aarohi_seq = []
    Avarohi_seq = []
    for i in range(1,5):
        for j in range(len(raga.aaroha)-i+1):
            Aarohi_seq.append(raga.aaroha[j:i+j])
    for i in range(1,5):
        for j in range(len(raga.avaroha)-i+1):
            Avarohi_seq.append(raga.avaroha[j:i+j])
    return Aarohi_seq , Avarohi_seq
Aarohi_seq, Avarohi_seq = seq_phrases(raga)

def mixed_phrases(raga:Raga, Aarohi_seq, Avarohi_seq):
    """Function to create all mixed phrases using helper functions"""
    pass

def freseqAA(raga:Raga, Aarohi_seq):
    mixedAA = []
    for p1,p2 in product(Aarohi_seq,Aarohi_seq):
        if raga.aaroha.index(p1[-1]) == raga.aaroha.index(p2[0])-1:
            if p1+p2 not in mixedAA:
                mixedAA.append(p1+p2)
            # print(p1+p2)
    return mixedAA
mixedAA = freseqAA(raga, Aarohi_seq)
def freseqDD(raga:Raga, Avarohi_seq):
    mixedDD = []
    for p1,p2 in product(Avarohi_seq,Avarohi_seq):
        if raga.avaroha.index(p1[-1]) == raga.avaroha.index(p2[0])-1:
            if p1+p2 not in mixedDD:
                mixedDD.append(p1+p2)
            # print(p1+p2)
    return mixedDD
mixedDD = freseqDD(raga, Avarohi_seq)
def freseqAD(Aarohi_seq, Avarohi_seq):
    mixedAD = []
    for p1,p2 in product(Aarohi_seq,Avarohi_seq):
        if raga.aaroha.index(p1[-1]) == raga.aaroha.index(p2[0])+1:
            if p1+p2 not in mixedAD:
                mixedAD.append(p1+p2)
    return mixedAD
mixedAD = freseqAD(Aarohi_seq,Avarohi_seq)
def freseqDA(Aarohi_seq, Avarohi_seq):
    mixedDA= []
    for p1,p2 in product(Avarohi_seq,Aarohi_seq):
        if raga.aaroha.index(p1[-1]) == raga.aaroha.index(p2[0])-1:
            if p1+p2 not in mixedDA:
                mixedDA.append(p1+p2)
    return mixedDA
mixedDA = freseqDA(Aarohi_seq,Avarohi_seq)
#generating meend phrases

def fremndAA(raga:Raga, lml:LML, Aarohi_seq):
    meendAA = []
    for p1,p2 in product(Aarohi_seq,Aarohi_seq):
        if p2[0] in lml.sga(s1=p1[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAA:
                meendAA.append(p1+p2)
        if p2[0] in lml.skga(s1=p1[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAA:
                meendAA.append(p1+p2)
        if p2[0] in lml.spa(s1=p1[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAA:
                meendAA.append(p1+p2)
        if p2[0] in lml.sma(s1=p1[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAA:
                meendAA.append(p1+p2)
        # if p2[0] in lml.ss(s1=p1[-1]):
        #     # print(p1+p2)
        #     if p1+p2 not in meendAA:
        #         meendAA.append(p1+p2)
    return meendAA

def fremndAV(raga:Raga, lml:LML, Avarohi_seq):
    meendAV = []
    for p1,p2 in product(Avarohi_seq,Avarohi_seq):
        if p1[0] in lml.sga(s1=p2[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAV:
                meendAV.append(p1+p2)
        if p1[0] in lml.skga(s1=p2[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAV:
                meendAV.append(p1+p2)
        if p1[0] in lml.spa(s1=p2[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAV:
                meendAV.append(p1+p2)
        if p1[0] in lml.sma(s1=p2[-1]):
            # print(p1+p2)
            if p1+p2 not in meendAV:
                meendAV.append(p1+p2)
        # if p2[0] in lml.ss(s1=p1[-1]):
        #     # print(p1+p2)
        #     if p1+p2 not in meendAA:
        #         meendAA.append(p1+p2)
    return meendAV

meendAV = fremndAV(raga, lml, Avarohi_seq)
# for i in meendAV:
#     print(i)

meendAA = fremndAA(raga, lml, Aarohi_seq)
# for i in meendAV:
#     print(i)

def ALM(raga:Raga, Aarohi_seq):
    ALM = []
    for i in raga.aaroha:
        ALM.append([i, i])
        ALM.append([i,i,i])
    for i in range(len(raga.aaroha)-1):
        ALM.append([raga.aaroha[i],raga.aaroha[i+1]])
        ALM.append([raga.aaroha[i],raga.aaroha[i+1],raga.aaroha[i],raga.aaroha[i+1]])
        ALM.append([raga.aaroha[i],raga.aaroha[i+1],raga.aaroha[i]])
    for i in range(len(raga.aaroha)-4):
        ALM.append([raga.aaroha[i],raga.aaroha[i+3], raga.aaroha[i+2],raga.aaroha[i+1]])
    return ALM

ALM_all = ALM(raga, Aarohi_seq)
# for i in ALM:
#     print(i)

def all_phrases(ALM,meendAA,meendAV,mixedDA,mixedAA,mixedAD,mixedDD):
    phrases = []
    for i in ALM:
        if i not in phrases:
            phrases.append(i)
    for i in meendAA:
        if i not in phrases:
            phrases.append(i)
    for i in meendAV:
        if i not in phrases:
            phrases.append(i)
    for i in mixedAA:
        if i not in phrases:
            phrases.append(i)
    for i in mixedAD:
        if i not in phrases:
            phrases.append(i)
    for i in mixedDA:
        if i not in phrases:
            phrases.append(i)
    for i in mixedDD:
        if i not in phrases:
            phrases.append(i)
    return phrases

phrases_all = all_phrases(ALM_all,meendAA,meendAV,mixedDA,mixedAA,mixedAD,mixedDD)
print(len(phrases_all))
# for phrase in phrases_all:
#     print(phrase)



    



    

