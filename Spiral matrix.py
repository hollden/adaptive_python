import numpy as np
# n = int(input())

n = 5
array = [[0] * n for i in range(n)]
# array[1] = 7
counter = 1
# array = np.rot90(array)
p_i = 0
p_j = 0
while counter <= n ** 2:

    for i in range(p_j, n):
        if array[p_i][i] != 0:
            p_j = n - p_i - 1
            p_i = n - i
            break
        array[p_i][i] = counter
        counter += 1
    else:
        p_j = 1

    array = np.rot90(array)

for row in array:
    print(' '.join([str(elem) for elem in row]))