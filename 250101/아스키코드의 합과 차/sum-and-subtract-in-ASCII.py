a, b =map(str, input().split())

a = ord(a)
b = ord(b)
c=  a-b
print(a+b, end=' ')
if a >= b:
    print(c)
else:
    print(-c)