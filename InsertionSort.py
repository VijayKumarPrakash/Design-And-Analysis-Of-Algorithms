def insertionSort(a, low, high):
    for i in range(2, len(a)):
        j = i-1
        x = a[i]
        while j >= 0:
            if x > a[j]:
                break
            j -= 1
        k = i-1
        while k > j:
            a[k+1] = a[k]
            k -= 1
        a[k+1] = x


a = [ 4, 11, 1, 17, 77, 9, 8]
insertionSort(a, 0, 5)
print(a)