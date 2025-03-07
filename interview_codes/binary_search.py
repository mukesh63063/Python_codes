
def binary_search(a, t):
    a.sort()
    n = len(a)
    l, r = 0, (n-1)
    while r>=l:
        m = l + (r-l)//2
        if a[m] == t:
            return m
        elif a[m] < t:
            l = m+1
        else:
            r = m-1
    return "Element is not in the list"

a = [1,90,20,4,6,0,7,11,12]
t =90
print(binary_search(a, t))