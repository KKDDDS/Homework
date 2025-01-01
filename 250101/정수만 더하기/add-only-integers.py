a = list(input())
sum = 0

for elem in a:
    if elem.isdigit():
        elem = int(elem)
        sum += elem

print(sum)