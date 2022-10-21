import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

prime = []
n = 2
while len(prime) <= 1001:
    if isPrime(n):
        prime.append(n)
    n += 1
N, X = map(int, input().split())
for i in range(0, N + 1):
    print(X, end=" ")
    X = X + prime[i]