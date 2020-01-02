l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=str(input())
for c1 in l:
    for c2 in range(len(s)):
        if c1==s[c2]:
            break
        if c2==s[len(s)-1]:
            print('nahi Hai')
            break
        else:
            continue
    if c2==s[len(s)-1]:
        break
if c1=='z':
    print('hai')
