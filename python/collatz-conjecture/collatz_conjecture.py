def steps(number):
    if number <= 0:
        raise ValueError("number should not be zero and negative.")
    step = 0
    if number == 1:
        return step
    while number != 1:
        if number&1:
            number = int((3 * number) + 1)
        else:
            number = int(number / 2)
        step += 1
    return step