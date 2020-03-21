number = int(input())
count, current_number = 1, 1
for i in range(number):
    if count > 0:
        print(current_number, end=' ')
        count -= 1
    else:
        count = current_number
        current_number += 1
        print(current_number, end=' ')

