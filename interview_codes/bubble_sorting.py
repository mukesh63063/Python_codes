
def bubble_sorting(a):

    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [1,90,20,4,6,0,7,11,12]
print(bubble_sorting(a))