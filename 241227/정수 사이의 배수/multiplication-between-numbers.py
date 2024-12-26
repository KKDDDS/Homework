a, b = map(int, input().split())
ans = 0
n = 0
for i in range(a, b+1):
    if i%5 ==0 or i%7 ==0:
        ans += i
        n += 1

print(f"{ans} {ans/n:.1f}") 