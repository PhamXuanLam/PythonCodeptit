T = int(input())
for t in range(T):
    dem = 0
    n = int(input())
    b = 1
    while (b * (b + 1) < 2 * n):
        a = (n - (b * (b + 1)) / 2) / (b + 1)
        if (a - int(a) == 0.0):
            dem += 1
        b += 1
    print(dem)