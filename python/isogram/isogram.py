def is_isogram(string):
    for _ in string:
        if (not(_.isalpha()) or string.lower().count(_.lower()) != 1) and _ != " " and  _ != "-":
            return False
    return True