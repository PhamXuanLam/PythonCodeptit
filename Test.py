a = []
x = 10
while x != 0:
    b = [int(i) for i in input().split()]
    for i in b:
        if a.__contains__(i % 42) == False:
            a.append(i % 42)
        x -= 1
print(len(a))