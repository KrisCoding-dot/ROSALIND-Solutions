Sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def count_nucleotides(sequence):
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nucleotide in sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    return nucleotide_counts

print(count_nucleotides(Sequence))