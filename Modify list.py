lst = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            l[i] = '*'
    for _ in range(l.count('*')):
        l.remove('*')



modify_list(lst)
print(lst)
