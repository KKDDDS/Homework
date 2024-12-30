N = int(input())

arr = list(map(int, input().split()))



while len(arr)>0:
    max_num  = -1
    for elem in arr:
        if elem > max_num:
            max_num = elem
        
    print(arr.index(max_num)+1, end=' ')
    arr = arr[:arr.index(max_num)]

