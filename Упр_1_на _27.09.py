a = int(input())
delitel = 2
while a > 1 and delitel <= a:
    if a % delitel == 0:
        print(delitel)
        while a % delitel == 0:
            a = a // delitel
    delitel += 1
