
def dem(a, b):
    s = 0
    while(b / 2 > a):
        s += 1
        if b % 2 == 0: b = b/2
        else: b = int(b/2) + 1
    return s

for t in range(int(input())):
    n = int(input())
    res = 0
    a = [int(i) for i in input().split()]
    for i in range(n - 1):
        x = min(a[i], a[i + 1])
        y = max(a[i], a[i + 1])
        if x*2 >= y: continue
        else: 
            d = dem(x, y)
            res += d
    print(res)
    