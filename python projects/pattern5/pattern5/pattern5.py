n=int(input())
k=(2*n)-2
for i in range(n+1):
    for j in range(k):
        print(" ",end='')
    k=k-1
    for j in range(i):
        print("* ",end='')
    print("\n")