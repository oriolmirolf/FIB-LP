def myLength(L):
    size = 0
    for i in L:
        size += 1
    return size

    # if L == []: return 0
    # return 1 + myLength(L[1:])