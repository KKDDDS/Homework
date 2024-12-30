arr = [
    [0]*5 for _ in range(5)
]

for n in range(5):
    arr[0][n] = 1

for m in range(5):
    arr[m][0] = 1

for j in range(1,5):
    for k in range(1,5):
        arr[k][j] = arr[k][j-1] + arr[k-1][j]

for l in arr:
    for elem in l:
        print(elem, end=' ')
    print()