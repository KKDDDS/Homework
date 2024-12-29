arr = list(map(float, input().split()))
sum = 0 

for i in range(8):
    sum += arr[i]

print(round(sum/8, 1))