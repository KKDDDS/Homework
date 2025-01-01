n = int(input())
sum1 = 0

for i in range(n):
    num = int(input())
    sum1 += num

sum1 = str(sum1)

sum1 = sum1[1:]+sum1[0]
print(sum1)

