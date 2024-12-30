n = int(input())
arr = list(map(int, input().split()))
revenue = 0
while arr:
    elem = arr.pop()
    for elem2 in arr:
        if elem-elem2 > revenue:
            revenue = elem-elem2
print(revenue)