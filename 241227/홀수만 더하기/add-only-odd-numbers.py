n = int(input())
ans = 0
for i in range(n):
    a = int(input())
    if a %2 ==1 and a%3 ==0:
        ans += a

print(ans)