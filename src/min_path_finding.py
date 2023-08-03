import time
from random import randint

def make_matrix(n):
    return [[randint(0,100) for i in range(n)] for j in range(n)]

test0 = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

test1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [10, 25, 5, 70, 11, 6, 7, 8, 9],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9, 8, 7, 6, 100, 4, 3, 2, 1],
         [9, 8, 7, 6, 5, 4, 3, 100, 1],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9, 8, 7, 6, 5, 100, 3, 2, 1],
         [9, 8, 7, 6, 5, 4, 3, 50, 1],
         [9, 8, 7, 6, 566, 4, 3, 50, 1]]

GEN_MATRIX_SIZE = 13

test3 =make_matrix(GEN_MATRIX_SIZE)
print(test3)

INVALID = "invalid"

def min(x1, x2, x3):
    if x1 == INVALID:
        if x2 == INVALID:
            if x3 == INVALID:
                print("error occurred")
                return -1
            else:
                return x3
        else:
            if x3 == INVALID:
                return x2
            else:
                return x2 if x2 <= x3 else x3
    else:
        if x2 == INVALID:
            if x3 == INVALID:
                return x1
            else:
                return x1 if x1 <= x3 else x3
        else:
            if x3 == INVALID:
                return x1 if x1 <= x2 else x2
            else:
                return min_3valid_int(x1,x2,x3)

def min_3valid_int(x1,x2,x3):
    if x1 <= x2:
        if x1 <= x3:
            return x1
        else:
            return x3
    else:
        if x2 <= x3:
            return x2
        else:
            return x3


def find_min_path(matrix, row, col):
    if row<0 or col<0:
        return INVALID
    elif row == 0 and col == 0:
        return matrix[row][col]
    else:
        return matrix[row][col] + \
            min(find_min_path(matrix, row-1, col),\
                find_min_path(matrix, row-1, col-1),\
                find_min_path(matrix, row, col-1))

def measure_time(func_pointer, matrix, row, col):
    # Start timer
    start_time = time.time()

    res = func_pointer(matrix, row, col)

    # End timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print("test matrix={}, row={}, col={}, result={}".format(matrix, row, col, res))
    print("Elapsed time: ", elapsed_time)


measure_time(find_min_path, test0, 2,2)
measure_time(find_min_path, test1, 2,2)
measure_time(find_min_path, test1, 8,8)

measure_time(find_min_path, test3, GEN_MATRIX_SIZE-1,GEN_MATRIX_SIZE-1)


for c in test0:
    print(c)