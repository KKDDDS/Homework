a = list(input())
s1 = a[0]
s2 = a[1]

for i in range(len(a)):
    if a[i] == s1:
        a[i] = s2
    elif a[i] == s2:
        a[i] = s1

ans = ''.join(a)
print(ans)