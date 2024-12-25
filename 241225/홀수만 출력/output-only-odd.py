a, b = map(int, input().split())
ans = a
for _ in range (a, b+1):
    if ans %2 ==1:
        print(ans, end=" ")
    ans += 1