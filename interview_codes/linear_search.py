
def linear_search(a, t):
    n = len(a)
    for i in range(n):
        if a[i] == t:
            return i
    return "Element is not in the list"

a = [1,90,20,4,6,0,7,11,12]
t =0
print(linear_search(a, t))
