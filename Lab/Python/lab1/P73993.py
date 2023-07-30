from functools import reduce

def evens_product(L):
    filtered_list = filter(lambda x: x % 2 == 0, L)
    return reduce(lambda acc, l: acc * l, filtered_list, 1)

def reverse(L):
    return reduce(lambda acc, l: [l] + acc, L, [])

def zip_with(f, L1, L2):
    return [f(x, y) for x, y in zip(L1, L2)]
    
def count_if (f, L):
    result = [x for x in L if f(x)]
    return len(result)

# print(evens_product([1,2,4,3]))
# print(reverse([1,2,3]))
# print(zip_with(lambda x, y: x * y, [1, 2, 3], [10, 2]))
# print(count_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))