n = int(input())
cnt = n
for i in range(2*n-1, 0, -1):
    for j in range(cnt):
        print("*", end=' ')
    if i > n:
        cnt -= 1
    else:
        cnt += 1
    print()