arr = list(map(int, input().split()))
ans = 0
for i in range(len(arr)):
    if arr[i] == 0:
        ans = i
    else:
        ans = len(arr)-1
    
for j in range(ans-1,-1,-1):
    print(arr[j], end=' ')
    
