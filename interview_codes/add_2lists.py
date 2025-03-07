l1 = [10,22,45,9]
l2 = [12,11,33,10]

sum_result = []
carry = 0
for i, j in zip(l1, l2):
    add = i+j+carry
    result = add%10
    carry = add//10
    sum_result.append(result)

if carry:
    sum_result.append(carry)
print("Final result:- ", sum_result)

