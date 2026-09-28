DNA = "GATGGAACTTGACTACGTAAATT" 

def transcribe_dna_to_rna(dna_sequence):
    rna_sequence = dna_sequence.replace("T", "U")
    return rna_sequence

rna_result = transcribe_dna_to_rna(DNA)
print("Original DNA sequence:", DNA)
print("Transcribed RNA sequence:", rna_result)
