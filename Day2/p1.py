import sys
lines=[]
total=0
for x in sys.stdin:
    lines.append(x.strip())
id=0
for x in lines:
    id+=1
    temp = x.split()
    temp.pop(0)
    reds=0
    blues=0
    greens=0
    valid=True
    for y in range(0,len(temp),2):
        if (temp[y+1][:-1]) == "green" or (temp[y+1]) == "green":
            temp1=int(temp[y])
            if temp1>13:
                valid=False
                break
        elif (temp[y+1][:-1]) == "blue" or (temp[y+1])=="blue":
            temp1=int(temp[y])
            if temp1>14:
                valid=False
                break
        elif (temp[y+1][:-1]) == "red" or (temp[y+1]) == "red":
            temp1=int(temp[y])
            if temp1>12:
                valid=False
                break
        else:
            print([temp[y+1]])
            print("error")
            exit()
    if valid:
        total+=id
print(total)