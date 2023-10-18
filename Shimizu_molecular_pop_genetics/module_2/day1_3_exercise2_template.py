
seq1 = "ATGC"
seq2 = "ATAT"
seq3 = "ATGC"

sequences = [seq1, seq2, seq3]

total_same = 0
total_diff = 0
for i in range(0, len(sequences)):
    for j in range(i+1, len(sequences)):
        same = 0
        diff = 0
        print(i, sequences[i], j, sequences[j], end="\t")
        seq1 = sequences[i]
        seq2 = sequences[j]
        
        for n1,n2 in zip(seq1,seq2):
            if n1 == n2:
                same += 1
            else:
                diff += 1
        total_same += same
        total_diff += diff
        print(f"same {same} diff {diff}")
        
        
        
print("total same = %d" % total_same)
print("total diff = %d" % total_diff)
