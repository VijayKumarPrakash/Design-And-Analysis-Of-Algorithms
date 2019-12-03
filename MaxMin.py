maxi = mini = max1 = min1 = 0

def maxmin(a, low, high, maxi, mini):
    if low == high:
        maxi = a[low]
        mini = a[low]
    elif low == high-1:
        if a[low] > a[high]:
            maxi = a[low]
            mini = a[high]
        else:
            maxi = a[high]
            mini = a[low]
    else:
        mid = int((high+low)/2)
        maxmin(a, low, mid, maxi, mini)
        maxmin(a, mid+1, high, max1, min1)
        print("Maximum: ", maxi)
        print("Minimum: ", mini)
        if max1 > maxi:
            maxi = max1
            print("Maximum: ", maxi)
        if min1 < mini:
            mini = min1
            print("Minimum: ", mini)
        


a = [2, 45, 23, 4554, 11, 98, 1, 32, 65]
maxmin(a, 0, 8, maxi, mini)
