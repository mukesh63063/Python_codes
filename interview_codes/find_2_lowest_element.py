
# Don't use predefined function or method

unique_elements = []

a = [1, 2, 4, 3, 2]
for i in a:
    if i not in unique_elements:
        unique_elements.append(i)
unique_elements.sort()

if len(unique_elements) >1:
    print(unique_elements[1])
else:
    print(None)



