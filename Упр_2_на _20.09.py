st = list(input().split())
print(*(st[(len(st) - 2 + int(i)) % len(st)] for i in st))