def is_armstrong_number(number):
    str_number = str(number)
    power = len(str_number)
    print(str_number, power)
    addition = 0
    for i in range(power):
        addition += pow(int(str_number[i]), power)
    return True if addition == number else False
