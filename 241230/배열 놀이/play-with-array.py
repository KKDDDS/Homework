n, q  = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(q):
    ans = list(map(int, input().split()))
    if ans[0] == 1:
        cnt = ans[1]
        print(arr[cnt-1])

    elif ans[0] == 2:
        for num in arr:
            if ans[1] == num:
                x = arr.index(num)
        if x !=0:
            print(x+1)
        else:
            print(0)
        x=0
    
    else:
        for j in range(ans[1]-1, ans[2]):
            print(arr[j], end=' ')
        print()
