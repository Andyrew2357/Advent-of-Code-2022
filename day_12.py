import numpy as np

with open("day_12.txt","r") as f:
    lines=f.readlines()
    lines=[s.strip() for s in lines]

m,n=len(lines),len(lines[0])
BIG=m*n

grid=np.zeros(shape=(m,n),dtype=int)
dist=BIG*np.ones(shape=(m,n),dtype=int)

for r in range(m):
    row=list(lines[r])

    if "S" in row:
        cr,cc=(r,row.index("S"))
        row[cc]="z"
    if "E" in row:
        er,ec=(r,row.index("E"))
        row[ec]="z"
    
    grid[r,:]=np.array([ord(ch) for ch in row])

visited=set()
dist[cr,cc]=0
dr=[0,-1,0,1]
dc=[1,0,-1,0]

while not (er,ec) in visited:
    visited.add((cr,cc))

    # update new preliminary distances
    for d in range(4):
        r,c=cr+dr[d],cc+dc[d]

        if (0<=r<m) and (0<=c<n):
            if (not (r,c) in visited) and (grid[r,c]<=grid[cr,cc]+1):

                dist[r,c]=min(dist[r,c],dist[cr,cc]+1)
    
    # find next open node
    best_dist=BIG+m+n
    for row in range(m):
        for col in range(n):

            if (row,col) in visited:
                continue
            
            ds=dist[row,col]+abs(row-er)+abs(col-ec)
            if ds<best_dist:
                best_dist=ds
                cr,cc=row,col
    
print(dist[er,ec])

# PART 2 just switches start to the end and makes any "a" a valid end. Copying code because I'm lazy

dist2=BIG*np.ones(shape=(m,n),dtype=int)
visited2=set()
dist2[er,ec]=0
cr,cc=er,ec

target = ord("a")
while True:
    visited2.add((cr,cc))

    if grid[cr,cc]==target:
        break

    # update new preliminary distances
    for d in range(4):
        r,c=cr+dr[d],cc+dc[d]

        if (0<=r<m) and (0<=c<n):
            if (not (r,c) in visited2) and (grid[r,c]+1>=grid[cr,cc]):

                dist2[r,c]=min(dist2[r,c],dist2[cr,cc]+1)
    
    # find next open node
    best_dist=BIG
    for row in range(m):
        for col in range(n):

            if (row,col) in visited2:
                continue

            if dist2[row,col]<best_dist:
                best_dist=dist2[row,col]
                cr,cc=row,col
    
print(dist2[cr,cc])
