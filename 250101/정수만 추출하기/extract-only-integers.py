a, b = map(str, input().split())

a = list(a)
b = list(b)
arr1 =[]
arr2 =[]

for elem1 in a:
    if elem1.isdigit():
        arr1.append(elem1)
    else:
        break
for elem2 in b:
    if elem2.isdigit():
        arr2.append(elem2)
    else:
        break


sum1 = int(''.join(arr1))
sum2 = int(''.join(arr2))
print(sum1+sum2)