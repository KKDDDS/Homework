sum = 0
cnt = 0
while True:
    n = int(input())
    if 20<=n<30:
        sum += n
        cnt += 1
    else:
        break

print(f"{sum/cnt:.2f}")
