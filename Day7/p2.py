from collections import defaultdict

MAP = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 0,
  'Q': 12,
  'K': 13,
  'A': 14,
}

with open('input.txt', 'r') as input:
  hands = []
  for line in input:
    hand, bid = line.rstrip().split(" ")
    numJokers = sum(1 for h in hand if h == 'J')
    hand = [MAP[c] for c in hand]
    mem = defaultdict(int)
    for n in hand:
      if n != 0:
        mem[n] += 1
    v, n = max((v, n) for n, v in mem.items()) if mem else (0, 0)
    mem[n] += numJokers

    numMatches = defaultdict(int)
    for v in mem.values():
      numMatches[v] += 1
    key = (numMatches[5], numMatches[4], numMatches[3], numMatches[2])
    
    hands.append((key, hand, int(bid)))
  hands = sorted(hands)

  print(sum((i + 1) * bid for i, (_, _, bid) in enumerate(hands)))