n = int(input())
ans = True

for i in range (2, n):
    if n%i ==0:
        ans = False


if ans == True:
    print("P")
else:
    print("C")