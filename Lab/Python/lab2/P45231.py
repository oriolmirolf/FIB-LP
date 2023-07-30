# Problema 1
def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b
        
def roots(x):
    yield x
    acc = x
    while True:
        acc = (1/2) * (acc + (x/acc))
        yield acc
        
def primes():
    L = []
    acc = 2
    
    while True:
        yield acc
        L.append(acc)
        while divisible(acc, L):
            acc += 1
        
def divisible(x, L):
    for elem in L:
        if x % elem == 0:
            return True
    return False
    
def hammings(): 
    for i in range(1, 6):
        yield i
        
    acc = 6
    L = []
    
    while True:
        yield acc
        acc += 1
        if isPrime(acc):
            L.append(acc)
        while (divisible(acc, L)):
            acc += 1

from heapq import *

def hammings2():
    q = []
    heappush(q, 1)
    ant = 0
    while True:
        val = heappop(q)
        if val != ant:
            yield val
            heappush(q, val*2)
            heappush(q, val*3)
            heappush(q, val*5)
        ant = val
            
def isPrime(n):
    if n <= 1:
        return False
    
    c = 2
    while c * c <= n:
        if n % c == 0:
            return False
        c += 1
    return True