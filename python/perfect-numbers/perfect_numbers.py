import math


def classify(number):
    if number <= 0:
        raise ValueError("Number must be Natural Number.")
    elif number == 1:
        return "deficient"
    else:
        addition = 1
        for i in range(2, number):
            if number % i == 0:
                addition += i

        if addition > number:
            return "abundant"
        elif addition < number:
            return "deficient"
        else:
            return "perfect"
    pass
