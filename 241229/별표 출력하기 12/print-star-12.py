n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j%2 ==0:
            if i <=j:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        else:
            if i==1:
                print("*",end=' ')
            else:
                print(" ",end=' ')
    print()