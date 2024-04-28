# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/209.py
def l(str1, str2, str3):
    str1_length = len(str1)
    str2_length = len(str2)
    str3_length = len(str3)
    dp_matrix = [
        [[0 for i in range(str3_length + 1)] for j in range(str2_length + 1)]
        for k in range(str1_length + 1)
    ]
    for i in range(1, str1_length + 1):
        for j in range(1, str2_length + 1):
            for k in range(1, str3_length + 1):
                if str1[i - 1] == str2[j - 1] and str1[i - 1] == str3[k - 1]:
                    dp_matrix[i][j][k] = dp_matrix[i - 1][j - 1][k - 1] + 1
                else:
                    dp_matrix[i][j][k] = max(
                        max(dp_matrix[i - 1][j][k], dp_matrix[i][j - 1][k]),
                        dp_matrix[i][j][k - 1],
                    )
    return dp_matrix[str1_length][str2_length][str3_length]
print(l("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"))