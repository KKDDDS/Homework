n, m = map(int, input().split())
cnt = 1
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n+m-1):
    for j in range(n):
        for k in range(m):
            if j+k == i:
                arr[j][k] = cnt
                cnt += 1

for l in arr:
    for elem in l:
        print(elem, end=' ')
    print()

