# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/158.py
def get_possible_paths(matrix):
    n, m = len(matrix), len(matrix[0])
    # possible_pathsetting the values of 1 to -1 as positive numbers are used to construct the
    # paths
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = -1
    # setting the vertical and horizontal paths
    for i in range(n):
        if matrix[i][0] == -1:
            break
        else:
            matrix[i][0] = 1
    for i in range(m):
        if matrix[0][i] == -1:
            break
        else:
            matrix[0][i] = 1
    # generating the paths
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != -1:
                possible_paths = 0
                if matrix[i - 1][j] != -1:
                    possible_paths += matrix[i - 1][j]
                if matrix[i][j - 1] != -1:
                    possible_paths += matrix[i][j - 1]
                matrix[i][j] = possible_paths
    return matrix[-1][-1]

matrix = [
    [0,0,1],
    [0,0,1],
    [1,0,0]
]
print(get_possible_paths(matrix))