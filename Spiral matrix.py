n = 25
arr = [[0] * n for _ in range(n)]


def print_arr(arr):
    for row in arr:
        print(*row)


def spiral(n, count, i, j, move, arr):
    if count != n ** 2 + 1:
        if move == 'right':
            for j_t in range(j, n):
                if arr[i][j_t] != 0:
                    j = j_t - 1
                    i += 1
                    break
                arr[i][j_t] = count
                count += 1
            else:
                j = n - 1
                i += 1
            # print('right')
            # print_arr(arr)
            spiral(n, count, i, j, 'down', arr)
        elif move == 'left':
            for j_t in range(j, -1, -1):
                if arr[i][j_t] != 0:
                    j = j_t + 1
                    i -= 1
                    break
                arr[i][j_t] = count
                count += 1
            else:
                i = n - 2
                j = 0
            # print('left')
            # print_arr(arr)
            spiral(n, count, i, j, 'up', arr)
        elif move == 'up':
            for i_t in range(i, -1, -1):
                if arr[i_t][j] != 0:
                    i = i_t + 1
                    j += 1
                    break
                arr[i_t][j] = count
                count += 1
            else:
                i = 0
                j = 0
            # print('up')
            # print_arr(arr)
            spiral(n, count, i, j, 'right', arr)
        else:
            for i_t in range(i, n):
                if arr[i_t][j] != 0:
                    i = i_t - 1
                    j -= 1
                    break
                arr[i_t][j] = count
                count += 1
            else:
                i = n - 1
                j = n - 2
            # print('down')
            # print_arr(arr)
            spiral(n, count, i, j, 'left', arr)





spiral(n, 1, 0, 0, 'right', arr)
print_arr(arr)

