def equilateral(sides):
    if check_triangle_inequality(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False


def isosceles(sides):
    if check_triangle_inequality(sides):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
    return False


def scalene(sides):
    if check_triangle_inequality(sides):
        if sides[0] != sides[1] != sides[2]:
            return True
    return False

def check_triangle_inequality(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    if sides[0]<=sides[1]+sides[2] and sides[1]<=sides[0]+sides[2] and sides[2]<=sides[0]+sides[1]:
        return True
    return False