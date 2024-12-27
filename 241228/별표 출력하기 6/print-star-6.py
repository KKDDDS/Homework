n = int(input())
cnt = 0
for i in range(2*n-1):
    for j in range(cnt):
        print(" ", end=' ')
    
    for j in range(2*n-cnt*2-1):
        print("*", end=' ')
    
    if i < n-1:
        cnt += 1
    else:
        cnt -= 1
    
    
    print()