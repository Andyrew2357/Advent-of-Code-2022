import numpy as np
import re

with open("day_11.txt","r") as f:
    lines=f.readlines()
    lines=[l.strip() for l in lines]

items=[]
monkey_ind=[]
personality={}
mod=1

for k in range(0,len(lines),7):
    it=[int(s) for s in re.split(r': |, ',lines[k+1])[1:]]
    for itt in it:
        items.append(itt)
        monkey_ind.append(k//7)
    op=(lines[k+2].split()[-3:])
    test=int(lines[k+3].split()[-1])
    partners=(int(lines[k+4].split()[-1]),int(lines[k+5].split()[-1]))
    personality[k//7]=(op,test,partners)
    mod*=test

num_monkeys=len(lines)//7 + 1
inspections=np.zeros(num_monkeys,dtype=np.int64)
items=np.array(items,dtype=np.int64)
monkey_ind=np.array(monkey_ind,dtype=np.int64)
num_it=10000

for _ in range(num_it):
    for ind in range(num_monkeys):
        op,test,partner=personality[ind]
        indices=np.where(monkey_ind==ind)[0]
        inspections[ind]+=len(indices)

        for k in indices:
            #inspect
            match op:
                case "old","*","old": items[k]*=items[k]
                case "old","*",x: items[k]*=int(x)
                case "old","+",x: items[k]+=int(x)
            
            #items[k]=items[k]//3 # part 1
            items[k]=items[k]%mod # part 2

            monkey_ind[k]=partner[0] if items[k]%test==0 else partner[1]

inspections=np.sort(inspections)
print(inspections[-1]*inspections[-2])

