# string = input()

code_string = '13ab4c2CaB'
numbers = '1234567890'
decode_string = ''
number = 1
string_number = ''
for elem in code_string:
    if elem in numbers:
        string_number += elem
    else:
        if string_number != '':
            number = int(string_number)
        decode_string += elem * number
        number = 1
        string_number = ''
print(decode_string)