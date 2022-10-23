
def factorial(n):
    sum = 1
    for i in range(2, n + 1):
        sum *= i
    return sum

def check(n):
    res = 0
    for i in n:
       res += factorial(int(i))
    if res == int(n):
        return "YES"
    else: return "NO" 

for t in range(int(input())):
    n = input()
    print(check(n)) 
