arr = list(map(int, input().split()))
print(arr[0], arr[1],end=' ')
for i in range(8):
    nn = (arr[i]+arr[i+1])%10
    arr.append(nn)
    print(nn, end=' ')
