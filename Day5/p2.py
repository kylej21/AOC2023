import time
start = time.time()

lines = [l.strip() for l in open("input.txt").readlines()]
tempSeeds = [int(i) for i in lines[0].split(':')[1].split()]
seeds=[]
for i in range(0,len(tempSeeds),2):
    for y in range(tempSeeds[i],tempSeeds[i]+tempSeeds[i+1]):
        if not y in seeds:
            seeds.append(y)
    
edited=[]
for x in lines[1:]:
    if x=="":
        edited=[0]*len(seeds)
        continue
    elif x[0] in "0123456789":
        temp = [int(x) for x in x.split()]
        start=temp[1]
        end=temp[1]+temp[2]
        displace=temp[0]-temp[1]
        for y in range(len(seeds)):
            if end>=seeds[y]>=start and edited[y]==0:
                seeds[y]=seeds[y]+displace
                edited[y]=1
print(min(seeds))
print("--- %s seconds ---" % (time.time() - start))
