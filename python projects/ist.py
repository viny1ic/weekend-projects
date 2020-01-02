d=['Sunday','Monday','Tuesday',"Wednesday","Thursday","Friday","Saturday"]
day=str(input())
hr=int(input())
mn=int(input())
tm=hr+mn
for c in range(len(d)-1):
    if day==d[c]:
        break
    elif d[c]=="saturday":
        print('Invalid input')
if hr>=24:
    print('Invalid input')
if mn>=60:
    print('Invalid input')
mni=mn +30
if mni>=60:
    mni=mni-60
    hr=hr+1
hri=hr+5
if hri>=24:
    hri=hri-24
    day=d[c+1]
print(day.rstrip())
print(hri)
print(mni)
