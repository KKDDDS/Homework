n = int(input())
cnt = 1
for i in range(1, n+1):
    if i%2 ==0:
        for j in range(1, n+1):
            if j==1:
                cnt += n-1
            print(cnt, end=' ')
            cnt -= 1
            if j==n:
                cnt +=n+1
    else:
        for k in range(1, n+1):
            print(cnt, end=' ')
            cnt += 1
    print()