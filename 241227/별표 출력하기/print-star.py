n = int(input())
x = 2*n
cnt = 1
for i in range(x):
    for j in range(cnt):
        print("*", end=' ')
    
    if i < n-1:
        cnt += 1
    else:
        cnt -= 1
    print()