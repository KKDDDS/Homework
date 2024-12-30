n = int(input())

arr=[
    [0 for _ in range(num+1)]
    for num in range(n)
]

for i in range(n):
    arr[i][0] = arr[i][i] = 1

for j in range(2, n):
    for k in range(1, j):
        arr[j][k] = arr[j-1][k-1]+arr[j-1][k]

for l in arr:
    for elem in l:
        print(elem,end=' ')
    print()