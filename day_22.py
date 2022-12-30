# just different rules for wrapping

import numpy as np
import re

with open("day_22.txt","r") as f:
    lines=f.readlines()
    m=lines.index("\n")
    n=max([len(s)-1 for s in lines[:m]])

    board=np.zeros(shape=(m,n),dtype=int)
    
    t={" ":-1,".":0,"#":1}

    wrap_r=-1*np.ones(shape=(n,2),dtype=int)
    wrap_c=-1*np.ones(shape=(m,2),dtype=int)

    for r in range(m):
        l=lines[r][:-1]
        for c in range(n):
            if c>=len(l): 
                board[r,c]=-1 
                continue
            e=t[l[c]]
            board[r,c]=e
            wrap_c[r,1]=c
            if e>=0 and wrap_c[r,0]==-1:
                wrap_c[r,0]=c
            if e>=0 and wrap_r[c,0]==-1:
                wrap_r[c,0]=r
            if e>=0 and r>wrap_r[c,1]:
                wrap_r[c,1]=r
    
    inst=lines[m+1].strip()
    inst=re.split("(\d+)",inst)[1:-1]

# Changing the wrapping pattern in part2. Doing some manual work, because I don't want to think about the cube folding problem.

cube_wrap_r=-1*np.ones(shape=(n,6),dtype=int)
cube_wrap_c=-1*np.ones(shape=(m,6),dtype=int)

for r in range(50):
    cube_wrap_c[r,:]=[149-r,0,0,149-r,99,2]

for r in range(50,100):
    cube_wrap_c[r,:]=[100,r-50,1,49,r+50,3]

for r in range(100,150):
    cube_wrap_c[r,:]=[149-r,50,0,149-r,149,2]

for r in range(150,200):
    cube_wrap_c[r,:]=[0,r-100,1,149,r-100,3]

for c in range(50):
    cube_wrap_r[c,:]=[c+50,50,0,0,c+100,1]

for c in range(50,100):
    cube_wrap_r[c,:]=[c+100,0,0,c+100,49,2]

for c in range(100,150):
    cube_wrap_r[c,:]=[199,c-100,3,c-50,99,2]

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
r,c=0,wrap_c[0,0]
d=0
dr=[0,1,0,-1]
dc=[1,0,-1,0]

visits=[]

i=0
for cmd in inst:
    if cmd.isalpha():
        if cmd=="R":
            d=(d+1)%4
        else:
            d=(d-1)%4
        continue
    
    for _ in range(int(cmd)):
        new_c=c+dc[d]
        new_r=r+dr[d]
        new_d=d

        if new_c>wrap_c[r,1]: new_r,new_c,new_d=cube_wrap_c[r,3:]
        elif new_c<wrap_c[r,0]: new_r,new_c,new_d=cube_wrap_c[r,:3]
        elif new_r>wrap_r[c,1]: new_r,new_c,new_d=cube_wrap_r[c,3:]
        elif new_r<wrap_r[c,0]: new_r,new_c,new_d=cube_wrap_r[c,:3]

        if board[new_r,new_c]==1: break

        r,c,d=new_r,new_c,new_d
        visits.append((r,c,d))

print("part2: ", 1000*(r+1)+4*(c+1)+d)

for r,c,d in visits: board[r,c]=5+d

from matplotlib import pyplot as plt
plt.imshow(board)
plt.tight_layout()
plt.show()

