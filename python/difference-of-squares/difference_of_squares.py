def square_of_sum(number):
    sum =  int(((number)*(number+1))/2)
    return int(sum*sum)

def sum_of_squares(number):
    return int(((number)*(number + 1)*(2*number + 1))/6)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
