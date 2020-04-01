n = int(input())
first_tower = [i for i in range(n, 0, -1)]
second_tower = list()
third_tower = list()
etalon = [i for i in range(n, 0, -1)]


def kuda_klast(arr1, arr2):
    if len(arr1) > 0 and len(arr2) > 0:
        return 'first' if arr1[-1] > arr2[-1] else 'second'
    elif len(arr1) == 0:
        return 'first'
    else:
        return 'second'


while True:
    if n % 2 == 0:
        # Первое действие
        if kuda_klast(first_tower,second_tower) == 'first':
            first_tower.append(second_tower.pop())
            print('2 - 1')
        else:
            second_tower.append(first_tower.pop())
            print('1 - 2')
        if third_tower == etalon:
            break
        # Второе действие
        if kuda_klast(first_tower, third_tower) == 'first':
            first_tower.append(third_tower.pop())
            print('3 - 1')
        else:
            third_tower.append(first_tower.pop())
            print('1 - 3')
        if third_tower == etalon:
            break
        # Третье действие
        if kuda_klast(second_tower, third_tower) == 'first':
            second_tower.append(third_tower.pop())
            print('3 - 2')
        else:
            third_tower.append(second_tower.pop())
            print('2 - 3')
        if third_tower == etalon:
            break

    else:
        # Первое действие
        if kuda_klast(first_tower, third_tower) == 'first':
            first_tower.append(third_tower.pop())
            print('3 - 1')
        else:
            third_tower.append(first_tower.pop())
            print('1 - 3')
        if third_tower == etalon:
            break
        # Второе действие
        if kuda_klast(first_tower, second_tower) == 'first':
            first_tower.append(second_tower.pop())
            print('2 - 1')
        else:
            second_tower.append(first_tower.pop())
            print('1 - 2')
        if third_tower == etalon:
            break
        # Третье действие
        if kuda_klast(second_tower, third_tower) == 'first':
            second_tower.append(third_tower.pop())
            print('3 - 2')
        else:
            third_tower.append(second_tower.pop())
            print('2 - 3')
        if third_tower == etalon:
            break

