n = int(input())
ans = False
for i in range(1, n+1):
    if n%i ==0:
        ans = True

if ans ==True:
    print("C")

else:
    [print("N")]
