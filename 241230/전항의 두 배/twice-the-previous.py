arr = list(map(int, input().split()))

for i in range(8):
    arr.append(arr[i+1]+(arr[i]*2))

for num in arr:
    print(num,end=' ')