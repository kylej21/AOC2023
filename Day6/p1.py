lines = [l.strip() for l in open("input.txt").readlines()]
otimes=lines[0].split()
otimes.pop(0)
times=[int(x) for x in otimes]
odist=lines[1].split()
odist.pop(0)
dist=[int(x) for x in odist]
total=1
for x in range(len(times)):
    temps=[]
    for y in range(times[x]):
        if y*(times[x]-y) > dist[x]:
            temps.append(y*(times[x]-y))
    total*=len(temps)
print(total)