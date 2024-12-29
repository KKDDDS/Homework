s, e = map(int, input().split())
cnt = 0
ans = 0
for i in range(s, e+1):
    for j in range(1, i+1):
        if i%j ==0:
            cnt += 1
    if cnt == 3:
        ans += 1
    cnt = 0

print(ans)
