arr = list(map(int, input().split()))
cnt = 0
ans = 0
for num in arr:
    if num == 0:
        break
    if num%2==0:
        cnt += 1
        ans += num

print(cnt, ans, sep=' ')
