n = int(input())
cnt = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i%j==0:
            cnt += 1
        else:
            continue
    if cnt ==0:
        print(i, end=' ')
    cnt = 0
