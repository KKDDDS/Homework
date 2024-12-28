n = int(input())
cnt = 1
for i in range(2*n-1):
    for j in range(n-cnt):
        print(" ",end='')
    
    for k in range(cnt*2-1):
        print("*", end='')

    if i < n-1:
        cnt += 1
    else:
        cnt -= 1
        
    print()
    
    
