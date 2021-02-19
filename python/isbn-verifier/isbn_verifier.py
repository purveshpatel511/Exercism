def is_valid(isbn):
    co_eff = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) < 10 or len(clean_isbn) >= 11:
        return False
    else:
        addition = 0
        for i in range(10):
            if clean_isbn[i] == "X" and i == 9:
                addition += co_eff[i] * 10
            elif clean_isbn[i] == "X" and i != 9:
                return False
            else:
                if clean_isbn[i].isdigit():
                    addition += int(clean_isbn[i]) * co_eff[i]
                else:
                    return False
        if addition % 11 == 0:
            return True
        else:
            return False
    pass
