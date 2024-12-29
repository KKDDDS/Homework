arr = list(map(int, input().split()))

cnt = 0

for num in arr:
    if num == 0:
        break
    else:
        cnt += 1
sum = 0 
for j in range(cnt):
    sum += arr[j]

print(f"{sum} {sum/cnt:.1f}")
