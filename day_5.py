import time
stime=time.perf_counter()

with open("day_5.txt","r") as f:
    lines=f.readlines()
    dirs=[l.strip().split(" ")[1:6:2] for l in lines[10:]]

    stacks=[]
    for k in range(1,34,4):
        new_stack=[]
        for i in range(8)[::-1]:
            s=lines[i][k]
            if not s==" ":
                new_stack.append(s)
        stacks.append(new_stack)

for d in dirs:

    n,start,target=[int(e) for e in d]
    start-=1
    target-=1
    moved=stacks[start][-n:]
    #moved=moved[::-1]
    stacks[start]=stacks[start][:-n]
    for e in moved:
        stacks[target].append(e)

res=""
for k in range(9):
    if not len(stacks[k]) == 0:
        res+=stacks[k][-1]

print(res)

print(time.perf_counter()-stime)
