sequence = "AAAACCCGGT"

def complement_dna(sequence):
    complement = ""
    for nucleotide in sequence:
        if nucleotide == "A":
            complement += "T"
        elif nucleotide == "T":
            complement += "A"
        elif nucleotide == "C":
            complement += "G"
        elif nucleotide == "G":
            complement += "C"
    return complement

reverse_complement = complement_dna(sequence)[::-1]
print("Original DNA sequence:", sequence)
print("Reverse complement DNA sequence:", reverse_complement)