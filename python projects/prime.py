num=1
count=2
for num in range(1,51):
    for count in range(2,num):
        z=num%count
        if z!=0:
            continue
        else:
            break
    if count==(num-1):
        print(num)
