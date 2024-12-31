a = list(input())
s = a[0]
s2 = a[1]
for i in range(len(a)):
    if a[i] == s2:
        a[i] = s

ans = ''.join(a)
print(ans)
