COLOR_CODE = {
    0: "black",
    1: "brown",
    2: "red",
    3: "orange",
    4: "yellow",
    5: "green",
    6: "blue",
    7: "violet",
    8: "grey",
    9: "white",
}

def color_code(color):
    for i in range(10):
        if COLOR_CODE[i] == color:
            return i
    pass


def colors():
    color = list()
    for i in range(10):
        color.append(COLOR_CODE[i])
    return color
    pass
