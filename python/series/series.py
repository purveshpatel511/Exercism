def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("Length is greater than series")
    else:
        return [series[i : i + length] for i in range(0, len(series) - length + 1)]
    pass
