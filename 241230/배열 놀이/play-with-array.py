n, q  = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(q):
    ans = list(map(int, input().split()))
    if ans[0] == 1:
        cnt = ans[1]
        print(arr[cnt-1])

    elif ans[0] == 2:
        idx = -1
        if ans[1] in arr:
            idx = arr.index(ans[1])
        print(idx+1)
    
    else:
        for j in range(ans[1]-1, ans[2]):
            print(arr[j], end=' ')
        print()
