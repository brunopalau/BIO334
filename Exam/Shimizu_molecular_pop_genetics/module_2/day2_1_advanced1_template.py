import sys

genome_size = 0
GC_count = 0
file = open(sys.argv[1])
for i,line in enumerate(file):
    if line.startswith(">"):
        continue
    line = line.strip()
    genome_size+=len(line)
    for n in line:
        if n == "G" or n == "C":
            GC_count += 1
    
file.close()

print("genome size =", genome_size, "bp")
print(f"GC content = GC count/genome size = {GC_count/genome_size}")

