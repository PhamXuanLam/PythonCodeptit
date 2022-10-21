for t in range(int(input())):
    n = int(input())
    used = []
    for i in range(0, 1001):
        used.append(0)
    for i in range(n):
        used[int(input())] += 1
    res = 0
    for i in range(0, 1001):
        if used[i] > 0:
            res = max(res, used[i])
    for i in range(0, 1001):
        if used[i] == res:
            print(i)
            break