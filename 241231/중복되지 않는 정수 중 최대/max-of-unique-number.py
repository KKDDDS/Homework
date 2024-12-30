N = int(input())
arr = list(map(int, input().split()))

max_num = -1

for elem in arr:
    if max_num < elem:
        count = 0
        for elem2 in arr:
            if elem2 == elem:
                count += 1
        
        if count == 1:
            max_num = elem

print(max_num)
    