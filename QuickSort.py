def quicksort(a, low, high):
    left = low
    right = high
    x = a[int((left+right)/2)]
    while left <= right:
        while x > a[left]:
            left+=1
        while x < a[right]:
            right-=1
        if left <= right:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
            left+=1
            right-=1
    if low < right:
        quicksort(a, low, right)
    if left < high:
        quicksort(a, left, high)


a = [9, 44, 32, 20, 8, 3, 2, 11, 25]  
quicksort(a,0,8)     
print(a)