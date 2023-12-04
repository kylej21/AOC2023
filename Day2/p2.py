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
    reds,blues,greens=0,0,0
    valid=True
    for y in range(0,len(temp),2):
        if (temp[y+1][:-1]) == "green" or (temp[y+1]) == "green":
            temp1=int(temp[y])
            if temp1>greens:
                greens=temp1
        elif (temp[y+1][:-1]) == "blue" or (temp[y+1])=="blue":
            temp1=int(temp[y])
            if temp1>blues:
                blues=temp1
        elif (temp[y+1][:-1]) == "red" or (temp[y+1]) == "red":
            temp1=int(temp[y])
            if temp1>reds:
                reds=temp1
        else:
            print([temp[y+1]])
            print("error")
            exit()
    total+=reds*greens*blues
print(total)