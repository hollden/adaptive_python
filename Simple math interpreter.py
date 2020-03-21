expression = input().split()
operator = expression[1]
a, b = int(expression[0]), int(expression[2])
if operator == 'plus':
    print(a + b)
elif operator == 'minus':
    print(a - b)
elif operator == 'multiply':
    print(a * b)
elif operator == 'divide':
    print(a // b)
