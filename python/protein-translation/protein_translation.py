PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    # "UAA": "STOP",
    # "UAG": "STOP",
    # "UGA": "STOP",
}


def proteins(strand):
    translate = list()
    a, b = 0, 3
    for i in range(len(strand) // 3):
        try:
            translate.append(PROTEINS[strand[a:b]])
        except KeyError:
            continue
        a += 3
        b += 3
    return translate
