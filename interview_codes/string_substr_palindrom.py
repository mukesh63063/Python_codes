

a = "ABCBDH"
separate_substr = a[1:4]

empty = ''
for i in separate_substr:
    empty = i+empty
if empty == separate_substr:
    print('Y')
else:
    print('N')


#===================================================================

a = [21,10,100,4,45,88,100,450, 450, 450]
unique_elements = []
for i in a:
    if i not in unique_elements:
        unique_elements.append(i)

dict_rpt = {i:a.count(i) for i in unique_elements}
print(dict_rpt)
max_second_repeated_element = [i for i,j in dict_rpt.items() if j == 2]
print("Second max repeated value :- ", max_second_repeated_element)




