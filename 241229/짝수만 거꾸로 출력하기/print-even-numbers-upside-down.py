n = int(input())
arr = list(map(int, input().split()))
ans = []
for num in arr:
    if num%2==0:
        ans.append(num)

for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=' ')
