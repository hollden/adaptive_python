one = ['    ',
       '   |',
       '   |',
       '    ',
       '   |',
       '   |',
       '    ']
two = [' -- ',
       '   |',
       '   |',
       ' -- ',
       '|   ',
       '|   ',
       ' -- ']
three = [' -- ',
         '   |',
         '   |',
         ' -- ',
         '   |',
         '   |',
         ' -- ']
four = ['    ',
        '|  |',
        '|  |',
        ' -- ',
        '   |',
        '   |',
        '    ']
five = [' -- ',
        '|   ',
        '|   ',
        ' -- ',
        '   |',
        '   |',
        ' -- ']
six = [' -- ',
       '|   ',
       '|   ',
       ' -- ',
       '|  |',
       '|  |',
       ' -- ']
seven = [' -- ',
         '   |',
         '   |',
         '    ',
         '   |',
         '   |',
         '    ']
eight = [' -- ',
         '|  |',
         '|  |',
         ' -- ',
         '|  |',
         '|  |',
         ' -- ']
nine = [' -- ',
        '|  |',
        '|  |',
        ' -- ',
        '   |',
        '   |',
        ' -- ']
zero = [' -- ',
        '|  |',
        '|  |',
        '    ',
        '|  |',
        '|  |',
        ' -- ']

numbers = {1: one,
           2: two,
           3: three,
           4: four,
           5: five,
           6: six,
           7: seven,
           8: eight,
           9: nine,
           0: zero}
input_numbers = [int(s) for s in input()]
# input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
output = [''] * 9

# Первый столбец
output[0] = 'x'
output[8] = 'x'
for i in range(1, 8):
    output[i] = '|'

# Заполняем вывод цифрами
for i in range(len(input_numbers)):
    output[0] = output[0] + '----'
    count = 1
    output[8] = output[8] + '----'
    for line in numbers[input_numbers[i]]:
        output[count] = output[count] + line
        count += 1
    if i != len(input_numbers) - 1:
        output[0] = output[0] + '-'
        output[8] = output[8] + '-'
        for i in range(1, 8):
            output[i] = output[i] + ' '

# Последний столбец
output[0] = output[0] + 'x'
output[8] = output[8] + 'x'
for i in range(1, 8):
    output[i] = output[i] + '|'

print('\n'.join(output))





