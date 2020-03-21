def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif x > 2:
        return (x - 2) ** 2 + 1
    else:
        return -x / 2


if __name__ == '__main__':
    print(f(x=4.5))