input_string = [word.lower() for word in input().split()]
for word in set(input_string):
    print(word, input_string.count(word))