a, b = map(int, input().split())

rst = [0]*4
while a >1:
    k = a%b
    rst[k] += 1
    a //= b
    
sum = 0
for num in rst:
    sum += num**2

print(sum)