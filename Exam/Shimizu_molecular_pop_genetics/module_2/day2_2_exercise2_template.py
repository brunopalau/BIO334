import sys

def load_fasta(fasta):
    with open(fasta) as fasta:
        sequences = []
        for line in fasta:
            if not line[0] == ">":
                sequences.append(line.rstrip())
    return sequences

def calc_pi(sequences):
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
    return pi

sequences = load_fasta(sys.argv[1])
print("pi =", round(calc_pi(sequences),4))


