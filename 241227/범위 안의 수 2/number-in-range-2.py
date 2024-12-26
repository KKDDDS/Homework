ans = 0
n = 0
for i in range(10):
    a = int(input())
    if 0 <= a <=200:
        ans += a
        n += 1

print(f"{ans} {ans/n:.1f}")
