A = input()
B = input()

T = True

for i in range(2):
    if A[i] != B[i]:
        T = False

if T ==True:
    print("true")

else:
    print("false")