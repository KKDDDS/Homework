n = int(input())
cnt = 0
for i in range(n):
    arr  = list(map(int, input().split()))
    sum = 0 
    for num in arr:
        sum += num
    if sum/4 >=60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)