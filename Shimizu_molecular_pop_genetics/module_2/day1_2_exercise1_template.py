
seq1 = "ATGCATGC"
seq2 = "ATGGATCC"

sequences = [seq1, seq2]

same = 0
diff = 0


for n1,n2 in zip(seq1,seq2):
    print(n1,n2)
    if n1==n2:
        same+=1
    else:
        diff+=1


print("same nucleotides : %d" % same)       # Show the total number of same characters
print("differnt nucleotides : %d" % diff)   # Show the total number of different characters  


