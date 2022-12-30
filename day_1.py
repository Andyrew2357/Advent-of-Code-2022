import numpy as np

with open("day_1_input.txt","r") as file:
    entries = file.readlines()

    cals=[]
    sum=0
    for l in entries:
        if l=="\n":
            cals.append(sum)
            sum=0
            continue
        sum+=int(l[:-1])
top=sorted(cals)[-3:]
print(top)
print(np.sum(top))