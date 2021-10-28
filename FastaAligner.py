#!/usr/bin/python3
"""
Title: FastaAligner.py
Date: 2021-10-19
Author: Yueqi Gong

Description:
    This program will output the scores,identity and gap percentages of sequence alignment from the input file

List of functions:
    NUCScore(seq1,seq2)
    IDScore(seq1,seq2)
    Gaps(seq1,seq2)

Procedure:
    1. define fuction for calculating alignment score
    2. define function for calculating identity
    3. define function for calculating gap percentages
    4. read the input file,create a dictionary, make id names as keys and sequences as values
    5. put keys and values in two separate lists
    6. take every two sequences and use the funtions to calculate scores
    7. output the results

Usage:
    calculate how well two sequences aligned with each other
"""

#input a scoring matrix for nucleotide alignment
import numpy
NUC=numpy.array([[1,-2,-1,-2,-1],

[-2,1,-2,-1,-1],

[-1,-2,1,-2,-1],

[-2,-1,-2,1,-1],

[-1,-1,-1,-1,0]])

BASE='ATGC-' # show the order of bases in the title of matrix

# function1: calculate the alignment score of two sequences
def NUCScore(seq1,seq2):
    scr=0
    seq_len=min(len(seq1),len(seq2)) # count the length of sequence
    for i in range(seq_len):
            nuc1=BASE.index(seq1[i].upper()) # find out which base is on the current position
            nuc2=BASE.index(seq2[i].upper())
            scr+=NUC[nuc1,nuc2] # find the corresponding score in the matirx
    return scr

# funtion2: calculate the identity of two sequences 
def IDScore(seq1,seq2):
    scr=0
    seq_len=min(len(seq1),len(seq2))
    for i in range(seq_len):
        if seq1[i]==seq2[i]: # count the number of matched positions
            scr+=1
            identity= scr/seq_len # calculate the identity
    return (' {:.2%}'.format(identity)) # output the percentage

# function3: calculate the percentage of gaps
def Gaps(seq1,seq2):
    global gap # I added this because of error"local variable 'gap' referenced before assignment" occurred
    scr=0
    seq_len=min(len(seq1),len(seq2))
    for i in range(seq_len):
        if (seq1[i] == '-' or seq2[i] == '-') and seq1[i] != seq2[i] :
            scr+=1 # count the number of gaps
            gap= scr/seq_len*100 # I didn't use the same one with function2 because ValueError occurred when I tried to run it
    return ('{:.2}%'.format(gap))


dict={} # make a new dictionary
f= open('score.extra.fna','r') #open input file
for line in f:
    if line.startswith('>'):#for the header line
        id = line.strip("\n")#take ids as keys for the dictionary
        seqs = ''
    else:
        seqs = seqs + line.strip("\n")#take sequences as the values
        dict[id]=seqs

# put values in a list
seqList =list(dict.values())
# put keys in a list
idList = list(dict.keys())
# when I make this lists I realized that dictionaries are unordered so it's a bit tricky to compare every two sequences.
# so I googled it and found out that in python version 3.8 dictionaries are actually ordered so I just went with it anyway.

i=0
output = open('output.txt','w') # open output file
while (i< len(seqList)): # take one sequence
    for k in range(i+1,len(seqList)): # take anotehr one
        score = NUCScore(seqList[i], seqList[k]) # use function1
        identity = IDScore(seqList[i],seqList[k]) # use function2
        gap = Gaps(seqList[i],seqList[k]) # use function3
        IDa= idList[i].strip('>') # take id
        IDb= idList[k].strip('>')
        # output to the file
        print(IDa,'-',IDb,' identity:', identity,', gap:', gap,', Score =',score,file=output)
    i = i+1
output.close() # close file



