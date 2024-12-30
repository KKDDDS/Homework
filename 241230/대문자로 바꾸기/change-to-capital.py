for _ in range(5):
    arr = list(map(str,input().split()))
    for i in range(len(arr)):
        print(arr[i].upper(), end=' ')
    print()