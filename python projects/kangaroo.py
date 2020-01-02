s1=str(input())
s2=str(input())
k=0
c2=0
for c in range(len(s1)):
    for c1 in range(len(s2)):
        if s1[c]==s2[c1]:
            for c2 in range(c1,len(s2)):
                if s1[c]==s2[c2]:
                    c=c+1
                    continue
                if c2==len(s2)-1:
                    print('True')
                    k=1
                    break  
            if k==1:
                break
        if k==1:
            break
    if k==1:
        break
if k==0:
    print('False')
