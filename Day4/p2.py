from collections import defaultdict
import sys
lines=[]
for x in sys.stdin:
    lines.append(x.strip())
copies = defaultdict(lambda: 1)
for i, line in enumerate(lines):
    copies[i]
    q = line.split(": ")[1].split(" | ")
    winning = q[0].split(" ")
    have = q[1].split(" ")
    total = 0
    for num in have:
        if num != "":
            if num in winning:
                total += 1
    cardswon = range(i + 1, i + 1 + total)
    for card in cardswon:
        copies[card] += copies[i]
print( sum(copies.values()))