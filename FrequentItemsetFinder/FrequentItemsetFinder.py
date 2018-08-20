import copy
import pandas as pd
from collections import defaultdict

def GetSubSeq(seq, i, count):
    return seq[i:i+count]

def FindSubSeq(subseq, seq):
    i, n, m = -1, len(seq), len(subseq)
    try:
        while True:
            i = seq.index(subseq[0], i + 1, n - m + 1)
            if subseq == seq[i:i + m]:
               return i
    except ValueError:
        return -1

def FIF(dataset, minSup=2, minLength=2, maxLength=5):
    frequencies = defaultdict(int)
    windowsize = minLength
    for si in range(len(dataset)):
        seq = dataset[si]
        if len(seq) >= minLength:
            while True:
                for i in range(0, len(seq)):
                    subseq = GetSubSeq(seq, i, windowsize)
                    if not tuple(subseq) in frequencies and len(subseq) >= minLength:
                        result = FIFInternal(dataset[si:], subseq)
                        frequencies[tuple(subseq)] = result[tuple(subseq)] 
                windowsize += 1
                if windowsize > maxLength:
                    windowsize = minLength
                    break

    frequentItems = {k:v for k, v in frequencies.items() if v >= minSup}
    return frequentItems
                
def FIFInternal(dataset, subseq):
    result = defaultdict(int)
    for seq in dataset:
        subidx = FindSubSeq(subseq, seq)
        if subidx != -1:
            result[tuple(subseq)] += 1
            
    return result

def ReplaceFrequents(db, frequents):
    for i in range(len(db)):
        seq = db[i]
        for item in frequents:
            itemset = list(item)     # {('a','b'):2, ('c','d'):3, (...)}
            subidx = FindSubSeq(itemset, seq)
            if subidx != -1:
                sub_list_start = subidx
                sub_list_end = subidx + len(itemset)
                replacement = "".join(itemset)
                seq[sub_list_start : sub_list_end] = [replacement]

db =  [
    ["a", "b", "c", "d"],
    ["a", "c", "b", "c"],
    ["b", "f", "d", "c", "b", "c"],
    ["a", "c", "b", "d"],
    ["f", "d", "c", "b", "c"],
    ["f", "d", "c"],
    ["g", "f", "d"],
    ["h", "f", "d"],
    ["i", "f", "d"]
]