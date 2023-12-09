lines = [l.strip() for l in open("input.txt").readlines()]
dir=lines[0]
lines.pop(0)
d= dict()
for x in lines:
    d[x[0:3]]=tuple((x[7:10],x[12:15]))
current="AAA"
directionsIter,steps=0,0
while current!="ZZZ":
    if directionsIter==len(dir):
        directionsIter=0
    choices=d[current]
    if dir[directionsIter]=='L':
        current=choices[0]
    else:
        current=choices[1]
    directionsIter+=1
    steps+=1
print(steps)
      