import turtle


def koch_turns(n):
    one_iteration = [60, -120, 60]
    turns = list()
    new_turns = list()
    while n > 0:
        for elem in turns:
            new_turns.extend(one_iteration)
            new_turns.append(elem)
        new_turns.extend(one_iteration)
        turns = new_turns
        new_turns = list()
        n -= 1
    return turns


def turtle_koch_curve(n, line_length=10):
    for move in koch_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
    turtle.forward(line_length)



# turtle_koch_curve(10)
for turn in koch_turns(int(input())):
    print('turn', turn)




