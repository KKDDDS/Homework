N = int(input())

for i in range(1, N+1):
    for j in range(i,0,-1):
        print(N-j+1, end=' ')
    print()
