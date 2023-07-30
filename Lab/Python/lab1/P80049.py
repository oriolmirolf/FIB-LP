def count_unique(L):
    return len(set(L))
    
# Ilegal?
def remove_duplicates(L):
   return list(set(L))

from functools import reduce

def flatten(L):
    return reduce(lambda acc, l: acc + l, L, [])

def flatten_rec(L):
    func = lambda acc, l: acc + flatten_rec(l) if isinstance(l, list) else acc + [l]
    return reduce(func, L, []) 
    
# print(count_unique([1, 3, 2, 2, 3, 4]))
# print(remove_duplicates([3, 1, 3, 2, 3, 2, 3, 4]))
# print(flatten([[2, 6], [8, 1, 4], [], [1]]))
# print(flatten_rec([3, [1], [], [4, [], [5, 3]], [2, 1]]))