a = list(input())
b = list(input())

while len(a)>0:
    for i in range(len(a)-len(b)+1):
        cnt = 0
        for j in range(len(b)):
            if a[i+j] == b[j]:
                cnt += 1

        if cnt == len(b):
            for k in range(len(b)):
                a.pop(i)
            break
            
    if cnt != len(b):
        ans = ''.join(a)
        print(ans)
        break
                