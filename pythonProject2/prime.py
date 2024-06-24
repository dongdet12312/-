import sys

def solve():
    M, N = map(int, sys.stdin.readline().rstrip().split())
    primes = [True] * (N + 1)
    primes[1] = False
    for i in range(2, N + 1):
        if primes[i]:
            for j in range(i * 2, N + 1, i):
                primes[j] = False
    for i in range(M, N + 1):
        if primes[i]:
            print(i)

solve()
