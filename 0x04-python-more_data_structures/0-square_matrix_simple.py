#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    my_new_matrix = [[num ** 2 for num in row] for row in matrix]

    return my_new_matrix
