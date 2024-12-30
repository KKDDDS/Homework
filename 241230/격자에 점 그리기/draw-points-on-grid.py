n, m = map(int, input().split())
arr = [
    [0]*n for _ in range(n)
]
cnt = 0
for i in range(m):
    r, c= map(int, input().split())
    cnt += 1
    arr[r-1][c-1] = cnt

for l in arr:
    for elem in l:
        print(elem,end=' ')
    print()

