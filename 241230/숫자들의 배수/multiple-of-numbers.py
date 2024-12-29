n = int(input())
cnt = 0
nn = 0
while cnt != 2:
    nn += n
    if nn%5 ==0:
        cnt += 1
    print(nn, end=' ')
    