def binarysearch(a, low, high, keyvalue):
    if low == high:
        if a[low] == keyvalue:
            return low
        else:
            return -1
    else:
        mid = int((high+low)/2)
        if a[mid] == keyvalue:
            return mid
        elif keyvalue > a[mid]:
            return binarysearch(a, low, mid-1, keyvalue)
        else:
            return binarysearch(a, mid+1, high, keyvalue)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = binarysearch(a, 0, 8, 1)
print("Element found at position", x)