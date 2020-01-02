n=str(input())
a=0
e=0
i=0
o=0
u=0
for c in n:
    if c=='a':
        a=1
    if c=='e':
        e=1
    if c=="i":
        i=1
    if c=='o':
        o=1
    if c=='u':
        u=1
    else:
        continue
if a==1 and e==1:
    if i==1 and o==1:
        if u==1:
            print("vowelgram")
        else:
            print('not vowelgram')
    else:
        print('not vowelgram')
else:
    print('not vowelgram')
