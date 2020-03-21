n, m = 4, 4
mine_field = [['.', '.', '*', '.'],
              ['*', '*', '.', '.'],
              ['.', '.', '*', '.'],
              ['.', '.', '.', '.']]
# n, m = [int(i) for i in input().split()]
# mine_field = list()
# for i in range(n):
#     mine_field.append([elem for elem in input()])

result_field = [['*' for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        count_mines = 0
        if mine_field[i][j] == '.':
            if j+1 < m:
                if mine_field[i][j+1] == '*':
                    count_mines += 1
            if i+1 < n and j+1 < m:
                if mine_field[i+1][j+1] == '*':
                    count_mines += 1
            if i+1 < n:
                if mine_field[i+1][j] == '*':
                    count_mines += 1
            if i+1 < n and j-1 >=0:
                if mine_field[i+1][j-1] == '*':
                    count_mines += 1
            if j-1 >= 0:
                if mine_field[i][j-1] == '*':
                    count_mines += 1
            if i-1 >= 0 and j-1 >= 0:
                if mine_field[i-1][j-1] == '*':
                    count_mines += 1
            if i-1 >= 0:
                if mine_field[i-1][j] == '*':
                    count_mines += 1
            if i-1 >= 0 and j+1 < m:
                if mine_field[i-1][j+1] == '*':
                    count_mines += 1
            result_field[i][j] = count_mines


for row in result_field:
    print(''.join([str(elem) for elem in row]))
