import sys
sys.setrecursionlimit(10000)

drop=set()

with open("day_18.txt","r") as f:
    l=f.readlines()
    m=len(l)
    mx,my,mz=0,0,0
    for k in range(m):
        x,y,z=((int(e) for e in l[k].strip().split(",")))
        mx=max(mx,x)
        my=max(my,y)
        mz=max(mz,z)
        drop.add((x,y,z))



exterior=set()
neighbors=[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def surface(x,y,z):
    exterior.add((x,y,z))
    ext_surf=0

    for dx,dy,dz in neighbors:
        n=(x+dx,y+dy,z+dz)

        if n in exterior: continue
        if not (-1<=n[0]<=mx+1 and -1<=n[1]<=my+1 and -1<=n[2]<=mz+1): continue

        if n in drop:
            ext_surf+=1
        else:
            ext_surf+=surface(x+dx,y+dy,z+dz)         

    return ext_surf

print(surface(-1,-1,-1))
