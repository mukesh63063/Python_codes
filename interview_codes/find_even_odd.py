
a = [1,5,10,45,8,11]

result = ["Even:- "+str(i) if i%2==0 else "Odd:- " + str(i) for i in a]
for i in result:
    print(i)
