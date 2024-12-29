arr = list(map(str, input().split()))

for i in range(10):
    if i==1 or i==4 or i==7:
        print(arr[i], end=' ')