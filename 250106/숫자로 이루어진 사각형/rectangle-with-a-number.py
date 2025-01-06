n = int(input())

# Write your code here!

def count(num):
    cnt = 1
    for i in range(num):
        for j in range(num):
            print(cnt, end=' ')
            cnt += 1
            if cnt == 10:
                cnt = 1
        print( )

count(n)