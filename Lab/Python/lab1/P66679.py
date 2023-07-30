def my_map(f, L):
    return [f(x) for x in L]
    
def my_filter(f, L):
    return [x for x in L if f(x)]

def factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def triplets(n):
    r = range(1, n + 1)
    return [(x, y, z) for x in r for y in r for z in r if x**2 + y**2 == z**2] 
    
# print(my_map(lambda x: x + 1, [1, 2, 3, 4]))
# print(my_filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]))
# print(factors(10))
# print(triplets(20))