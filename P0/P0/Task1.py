"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
dir=[]
ans=0
for i in texts:
    if i[0] not in dir:
        dir.append(i[0])
        ans+=1
    if i[1] not in dir:
        dir.append(i[1])
        ans+=1
for i in calls:
    if i[0] not in dir:
        dir.append(i[0])
        ans+=1
    if i[1] not in dir:
        dir.append(i[1])
        ans+=1
print("There are",ans, "different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
