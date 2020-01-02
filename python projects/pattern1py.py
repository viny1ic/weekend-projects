count1=1
count2=1
for count1 in range(11):
    for count2 in range(count1+1):
        if count2!=(count1):
            print('*', end=(' '))
        else:
            print('\n')
