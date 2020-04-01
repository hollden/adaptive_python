n, m = [int(i) for i in input().split()]

arr = list()

for _ in range(n):
    arr.append(input().split())
transporte = zip(*arr)
for row in transporte:
    print(*row)

