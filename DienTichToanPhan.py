T = int(input())
for t in range(T):
    tong=0
    n,m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        b=[int(j) for j in input().split()]
        a.append(b)
    for i in range(n):
        for j in range(m):
            if a[i][j]!=0:
                tong += a[i][j]*4+2
                if(j!=m-1):
                    if (i != n - 1):
                        tong -=2 * min(a[i][j],a[i+1][j])
                    tong -=2 * min(a[i][j],a[i][j+1])
                else:
                    if (i != n - 1):
                        tong -=2 * min(a[i][j],a[i+1][j])
    print(tong)
