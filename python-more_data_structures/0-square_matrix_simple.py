#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print(map(lambda x: x**2 for row in matrix for i in row(i)))
