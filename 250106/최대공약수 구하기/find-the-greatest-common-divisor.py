n, m = map(int, input().split())

# Write your code here!
def num(a, b):
    while b>0:
        a, b = b, a%b
    print(a)

num(n,m)