# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/062.py
def get_num_ways(n: int, m: int) -> int:
    matrix = [[(1 if (i == 0 or j == 0) else 0) for i in range(m)] for j in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[n - 1][m - 1]
