alphabet = ' abcdefghijklmnopqrstuvwxyz'
# print(22 + 1 % 27 - 27 - 1)
# print(2 - 1 % 27 + 27) # 24
offset = int(input())
in_str = input()
result = ''
for elem in in_str:
    if offset > 0:
        result += alphabet[(alphabet.index(elem) + offset) % 27]
    else:
        result += alphabet[27 + (alphabet.index(elem) - offset) % 27]
    # if offset > 0 and alphabet.index(elem) + offset > 27:
    #     result += alphabet[alphabet.index(elem) + offset % 27 - 27 - 1]
    # elif offset > 0:
    #     result += alphabet[alphabet.index(elem) + offset]
    # elif offset < 0 and alphabet.index(elem) + offset < 0:
    #     result += alphabet[alphabet.index(elem) + offset % 27 + 27]
    # else:
    #     result += alphabet[alphabet.index(elem) + offset]
print('Result: "', result, '"', sep='')