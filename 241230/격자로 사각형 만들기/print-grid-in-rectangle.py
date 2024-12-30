n = int(input())

arr = [
    [0]*n for _ in range(n)
]

for i in range(n):
    arr[i][0] = 1
    arr[0][i] = 1

for j in range(1, n):
    for k in range(1, n):
        arr[j][k] = arr[j-1][k]+arr[j][k-1]+arr[j-1][k-1]

for l in arr:
    for elem in l:
        print(elem, end=' ')
    print()