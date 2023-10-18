
import sys

genome_size = 0

file = open(sys.argv[1])
for i,line in enumerate(file):
    if line.startswith(">"):
        continue
    line = line.strip()
    genome_size+=len(line)
    
file.close()

print("genome size =", genome_size, "bp")

