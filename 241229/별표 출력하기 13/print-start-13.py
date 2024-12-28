n = int(input())
cnt1 = 0
cnt2 = 1
for i in range(n, 0, -1):
    if i%2 ==1:
        for j in range(n-cnt1):
            print("*", end=' ')
        
        cnt1 += 1
            
    
    else:
        for k in range(cnt2):
            print("*", end=' ')
        cnt2 += 1
    
    print()

cnt1 -= 1
cnt2 -= 1

for l in range(1, n+1):
    if l%2 ==1:
        for m in range(n-cnt1):
            print("*", end=' ')
        
        cnt1 -=1
    
    else:
        for z in range(cnt2):
            print("*", end=' ')
        cnt2 -= 1
    print()