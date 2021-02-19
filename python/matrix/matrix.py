class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.int_matrix = list()
        for x in rows:
            sub_matrix = list()
            for i in x.split():
                sub_matrix.append(int(i))
            self.int_matrix.append(sub_matrix)
        pass

    def row(self, index):
        return self.int_matrix[index - 1]
        pass

    def column(self, index):
        col = list()
        for row in self.int_matrix:
            col.append(row[index - 1])
        return col
        pass