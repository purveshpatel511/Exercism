def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("String length is not equal.")
    if len(strand_a) == 0 and len(strand_b) == 0:
        return 0
    count = 0
    for x,y in zip(strand_a,strand_b):
        if x != y:
            count += 1
    return count