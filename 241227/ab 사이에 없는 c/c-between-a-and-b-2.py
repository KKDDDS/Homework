a, b, c = map(int, input().split())
ans = True
for i in range(a, b+1):
    if i%c ==0:
        ans = False

if ans == True:
    print("YES")
else:
    print("No")