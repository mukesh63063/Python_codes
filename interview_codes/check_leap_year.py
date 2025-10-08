# n = int(input("Enter years:- "))
n = 2025

if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
    print("Y")
else:

    print("N")
