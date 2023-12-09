lines = [l.strip() for l in open("input.txt").readlines()]

def go(arr):
    if len(arr)==arr.count(arr[0]):
        return arr[0]
    else:
        temp = []
        for y in range(len(arr)-1):
            temp.append(arr[y+1]-arr[y])
        arr.append(go(temp)+arr[-1])
        return arr[-1]
total=0
for x in lines:
    temp= [int(y) for y in x.split()]
    z=temp[::-1]
    
    total+=go(z)

print(total)
