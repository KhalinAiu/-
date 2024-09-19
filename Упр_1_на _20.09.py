st = input().split()
for i in range(1, len(st), 2):
    print(st[i], st[i - 1], st[i + 1] if i + 2 == len(st) else '', end="")