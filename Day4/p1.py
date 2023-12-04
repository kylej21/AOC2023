import sys
lines=[]
for x in sys.stdin:
    lines.append(x.strip())
trueTotal=0
last=1
for x in lines:
    temp = x.split()
    temp.pop(0)
    temp.pop(0)
    winning=[]
    barFound=False
    total=0
    for x in temp:
        if x=='|':
            barFound=True
        elif barFound == False:
            winning.append(x)
        else:
            if x in winning:
                if total==0:
                    total=1
                else:
                    total*=2
    trueTotal+=total    
print(trueTotal)