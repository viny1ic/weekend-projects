con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
st=str(input())
for c in con:
    x=0
    for c1 in st:
        if c==c1:
            x=x+1
            continue
        else:
            continue
    if x!=1:
        print('nahi hai')
        break
    elif c=='z':
        print('hai')
        break