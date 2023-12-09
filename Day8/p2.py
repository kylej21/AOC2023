import math,re
cmd, _, *lines = [re.findall(r"[\w]+", x) for x in open(0)]
lines = [l.strip() for l in open("input.txt").readlines()]
dir = lines[0]
d = dict()
for line in lines[2:]:
	line = line.split()
	d[line[0]] = [line[2][1:-1], line[3][:-1]]
def numsteps(x):
	i = 0
	while x[-1] != 'Z':
		x = d[x][0] if dir[i % len(dir)] == 'L' else d[x][1]
		i += 1
	return i
x = list(filter(lambda x: x[-1] == 'A', d.keys()))
print(math.lcm(*list(map(numsteps, x))))