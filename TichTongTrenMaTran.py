n, m, k = [int(i) for i in input().split()]
a = []
mod = 10**9 + 7
cnt = 1
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(cnt)
        cnt += 1
for q in range(k):
    x, y, z = [i for i in input().split()]
    res = 0
    if x == 'R':
        for i in range(m):
            a[int(y)][i] = a[int(y)][i]*int(z)
    else:
        for i in range(n):
            a[i][int(y)] = a[i][int(y)]*int(z)
    for i in range(n):
        for j in range(m):
            res += a[i][j] % mod
    print(res)
        
