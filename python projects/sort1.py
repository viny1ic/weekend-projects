l=int(input('enter length of the array: '))
lis=[]
for c in range(l):
    x=int(input('enter element: '))
    lis.append(x)
print(lis)
for i in range(l):
    for K in range(l-i-1):
        if lis[K]>lis[K+1]:
            t=lis[K]
            lis[K]=lis[K+1]
            lis[K+1]=t
print(lis)
