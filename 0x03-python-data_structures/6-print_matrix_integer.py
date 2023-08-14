#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for k in m:
            print("{:d}".format(k), end=" " if k != m[-1] else "")
        print()
