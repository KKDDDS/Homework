sum = 0
cnt = 0
while True:
    n = int(input())
    if n >= 30:
        break
    sum += n
    cnt += 1
if sum == 0:
    print(0)
else:
    print(f"{sum/cnt:.2f}")
