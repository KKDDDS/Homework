a, b = map(int, input().split())
ans = 0
if a<=b:
    for i in range(a, b+1):
        if i%5 ==0:
            ans += i
else:
    for i in range(b, a+1):
        if i%5 ==0:
            ans += i

print(ans)