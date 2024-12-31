a = input()
t = input()

aa = len(a)
tt = len(t)



for i in range(aa-tt+1):
    ans = True
    for j in range(tt):
        if a[i+j] != t[j]:
            ans = False
    
    if ans == True:
        print(i)
        break

if ans == False:
    print(-1)
        