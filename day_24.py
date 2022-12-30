# First Approach: pathfinding with memoization. I expect the actual number of possible paths is smaller
# than one would think, because it looks like blizzards block most connections at any given time.

import math
from collections import deque

# The blizzards can be stationary, we just need to move whatever position we're checking in the 
# opposite directions.
N_B=set()
S_B=set()
W_B=set()
E_B=set()

with open("day_24.txt","r") as f:
    lines=f.readlines()
    lines=[s.strip() for s in lines]
    M,N=len(lines),len(lines[0])
    Rt=(M-2)*(N-2)
    for r,l in enumerate(lines):
        if r==0 or r==M-1: continue
        for c,ch in enumerate(l):
            if c==0 or c==N-1: continue
            match ch:
                case ".": continue
                case "^": N_B.add((r,c))
                case "v": S_B.add((r,c))
                case "<": W_B.add((r,c))
                case ">": E_B.add((r,c))

ans=math.inf

SEEN={}
Q=deque([(0,1,0)])

adj=[(0,1),(1,0),(0,0),(-1,0),(0,-1)]

while Q:
    if len(SEEN)%10000==0: print(len(SEEN))

    r,c,t=Q.popleft()
    tf=t%Rt

    if (r,c,tf) in SEEN and t>=SEEN[(r,c,tf)]: continue
    SEEN[(r,c,tf)]=t

    # if you can finish, do so
    t+=1
    if r==M-2 and c==N-2: ans=min(ans,t)

    for dr,dc in adj:
        nr,nc=r+dr,c+dc

        # check for wall collisions
        if nr<1 and (not (nr,nc)==(0,1)): continue
        if nr>M-2 or nc<1 or nc>N-2: continue 

        # check for blizzard collisions

        # North and South
        if ((nr-1+t)%(M-2)+1,nc) in N_B or ((nr-1-t)%(M-2)+1,nc) in S_B: continue
        # West and East
        if (nr,(nc-1+t)%(N-2)+1) in W_B or (nr,(nc-1-t)%(N-2)+1) in E_B: continue

        Q.append((nr,nc,t))

print(ans)

