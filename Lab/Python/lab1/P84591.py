def absValue(x):
    if x > 0:
        return x
    else:
        return -x
        
def power(x, p):
    if p == 0:
        return 1

    aux = power(x, p//2)
    if p % 2 == 0:
        return aux * aux
    else:
        return aux * aux * x

def isPrime(n):
    if n <= 1:
        return False

    c = 2
    while c * c <= n:
        if n % c == 0:
            return False
        c +=1
    return True

def slowFib(n):
    if n < 2:
        return n
    
    return slowFib(n-1) + slowFib(n-2)

def quickFib(n):
    if n == 0: return 0

    first = 0
    second = 1

    while n > 1:
        n -= 1
        aux = second
        second = first + second
        first = aux

    return second