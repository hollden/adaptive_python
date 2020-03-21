input_numbers = [int(number) for number in input().split()]
# input_numbers = [4, 8, 0, 3, 4, 2, 0, 3]
for number in set(input_numbers):
    if input_numbers.count(number) > 1:
        print(number, end=' ')

