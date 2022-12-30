#PART 1

visited={(0,0)}

h=(0,0)
t=(0,0)
dirs={'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

for cmd in open("day_9.txt","r"):
    d,n=cmd.strip().split()
    n=int(n)
    for _ in range(n):
        h=(h[0]+dirs[d][0],h[1]+dirs[d][1])

        if abs(h[0]-t[0])<=1 and abs(h[1]-t[1])<=1:
            continue
        
        if not t[1]==h[1]:
            t=(t[0],t[1]+1) if t[1]<h[1] else (t[0],t[1]-1)
        if not t[0]==h[0]:
            t=(t[0]+1,t[1]) if t[0]<h[0] else (t[0]-1,t[1])
    
        visited.add(t)

print(len(visited))


#PART 2

import numpy as np

visited={(0,0)}

rope=np.zeros(shape=(10,2))
dirs={'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

for cmd in open("day_9.txt","r"):
    d,n=cmd.strip().split()
    n=int(n)
    for _ in range(n):
        rope[0,0]+=dirs[d][0]
        rope[0,1]+=dirs[d][1]

        for k in range(1,10):
        
            if max(abs(rope[k-1,:]-rope[k,:]))<=1:
                continue
            
            if not rope[k,0]==rope[k-1,0]:
                rope[k,0]=rope[k,0]+1 if rope[k,0] < rope[k-1,0] else rope[k,0]-1
            if not rope[k,1]==rope[k-1,1]:
                rope[k,1]=rope[k,1]+1 if rope[k,1] < rope[k-1,1] else rope[k,1]-1

        visited.add(tuple(rope[9,:]))

print(len(visited))
