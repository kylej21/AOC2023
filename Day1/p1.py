import sys
lines=[]
for x in sys.stdin:
  lines.append(x.strip())
total=0
for x in lines:
  temp=""
  for y in x:
    if y.isdigit():
      temp+=y
      break
  temp2=x[::-1]
  for z in temp2:
    if z.isdigit():
      temp+=z
      break
  total+=int(temp)
print(total)