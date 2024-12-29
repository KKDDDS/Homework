arr = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(10):
    if i%2==0:
        sum1 += arr[i]
    else:
        sum2 += arr[i]

if sum1 >= sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)