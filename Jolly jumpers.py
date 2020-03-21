# input_numbers = [int(i) for i in input().split()]
input_numbers = [int(n) for n in '1 3 5'.split()]
absolute_diff = list()
for i in range(len(input_numbers)-1):
    a = input_numbers[i]
    b = input_numbers[i+1]
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        absolute_diff.append(abs(a-b))
    else:
        absolute_diff.append(abs(a)+abs(b))
for i in range(1, len(input_numbers)):
    if i not in absolute_diff:
        print('Not jolly')
        break
else:
    print('Jolly')

