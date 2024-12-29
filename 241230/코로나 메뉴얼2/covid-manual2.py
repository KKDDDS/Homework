nt = [0]*4

for i in range(3):
    arr = list(input().split())
    w = str(arr[0])
    t = int(arr[1])
    if w=="Y" and t>=37:
        nt[0] += 1
    elif w=="N" and t>=37:
        nt[1] += 1
    elif w=="Y" and t<37:
        nt[2] += 1
    else:
        nt[3] += 1

for j in nt:
    print(j, end=' ')

if nt[0]>=2:
    print("E")