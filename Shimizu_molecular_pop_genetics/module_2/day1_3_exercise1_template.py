
seq1 = "ATGC"
seq2 = "ATAT"
seq3 = "ATGC"

sequences = [seq1, seq2, seq3]

for i in range(0, len(sequences)):
    for j in range(i+1, len(sequences)):
        seq1 = sequences[i]
        seq2 = sequences[j]
        equal = True
        for n1,n2 in zip(seq1,seq2):
            if n1 != n2:
                equal = False
                print(f"{i} {seq1} {j} {seq2} different")
                break
        if equal:
            print(f"{i} {seq1} {j} {seq2} same")
        
