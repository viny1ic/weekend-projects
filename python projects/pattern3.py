count1=1
count2=1
rev=1
for count1 in range(10,0,-1):
    for count2 in range(10,0,-1):
        if count2>rev:
            print(' ',end='')
        elif count2<=rev:
            print('*',end='')
    rev=rev+1
    print('\n')
