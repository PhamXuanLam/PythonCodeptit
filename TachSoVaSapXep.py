n = int(input())
a = []
for i in range(n):
    s = input()
    tmp = ""
    for j in s:
        if j >= '0' and j <= '9':
            tmp += j
        elif tmp != "":
            a.append(int(tmp))
            tmp = ""
    if tmp != "":
        a.append(int(tmp))
a.sort()
for i in a:
    print(i)
    