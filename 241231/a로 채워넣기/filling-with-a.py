a = list(input())

for i in range(len(a)):
    if i==1 or i==len(a)-2:
        a[i] ='a'

s = ''.join(a)
print(s)