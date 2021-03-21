def saddle_points(matrix):
    if len(matrix) == 0:
        return []

    ## Raise ValueError if nested list element is not match in case irregular matrix.
    element_count = len(matrix[0])
    for sublist in matrix:
        if len(sublist) != element_count:
            raise ValueError("Irregular Matrix.")

    ## column formation
    col_matrix = list()
    for i in range(len(matrix[0])):
        temp = list()
        for sublist in matrix:
            temp.append(sublist[i])
        col_matrix.append(temp)
    
    # output_list
    output = list()

    # find saddle point
    for r,ri in zip(matrix,range(len(matrix))):
        for c,ci in zip(col_matrix,range(len(col_matrix))):
            if sorted(r)[-1] == sorted(c)[0]:
                output.append({
                    "row": ri+1,
                    "column": ci+1
                })

    return output

saddle_points([])