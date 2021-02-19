def to_rna(dna_strand):
    output = ""
    for i in dna_strand:
        if i == "T":
            output += "A"
        if i == "G":
            output += "C"
        if i == "C":
            output += "G"
        if i == "A":
            output += "U"
    return output