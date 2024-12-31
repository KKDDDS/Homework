a = input()
t = input()

aa = len(a)
tt = len(t)

cnt = 0

for i in range(aa-tt+1):
    ans = True
    for j in range(tt):
        if a[i+j] != t[j]:
            ans = False
    
    if ans == True:
        cnt += 1

print(cnt)
        