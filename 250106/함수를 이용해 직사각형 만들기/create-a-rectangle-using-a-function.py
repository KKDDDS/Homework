n, m = map(int, input().split())

# Write your code here!

def print_1(a,b):
    for i in range(a):
        for j in range(b):
            print(1, end='')
        print()

print_1(n, m)