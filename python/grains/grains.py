def count_grain(number):
    grain, total_grain = 1, 1
    for i in range(2, number + 1):
        grain *= 2
        total_grain += grain
    return grain, total_grain

def square(number):
    if number <= 0 or number >= 65:
        raise ValueError("Square number must be between 1 to 64 inclusive.")
    elif number == 1:
        return 1
    else:
        grain, total_grain = count_grain(number)
        return grain

def total():
    grain, total_grain = count_grain(64)
    return int(total_grain)
