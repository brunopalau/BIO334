

import sys


sequences = []
file = open(sys.argv[1])
for line in file:
    if not line[0] == ">":
        sequences.append(line.rstrip())
file.close()


total_diff = 0
for i,seq1 in enumerate(sequences):
    for j,seq2 in enumerate(sequences[i+1:]):
        for n1,n2 in zip(seq1,seq2):
            if n1 != n2:
                total_diff +=1
                

    

num_sequences = len(sequences)
len_sequence = len(sequences[0])
combination = num_sequences*(num_sequences-1)/2
pi = total_diff/combination/len_sequence
print("total differences =", total_diff)
print("nC2 =", combination)
print("Lenght of sequence =", len_sequence)
print("pi =", pi)


