a = input()
b =''
for i in range(len(a)):
    if i%2==1:
        b += a[i]

for j in range(len(b)-1, -1, -1):
    print(b[j],end='')