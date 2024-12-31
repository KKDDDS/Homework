a, b = map(str, input().split())

s = a[0:2]
b = list(b)

for i in range(len(b)):
    if i < 2:
        b[i]=s[i]
        
ans = ''.join(b)
print(ans)