# THIS IS NOT EFFICIENT AT ALL BUT I DIDN'T WANT TO THINK ABOUT HOW TO OPTIMIZE
# The proper way to do this would be to look for the intersection of four sensor boundaries,
# but this runs decently quickly since my part 1 is fast, so I don't care to look back at it.

import re

#parse the input
scan={}
dist={}
MAX=4000000
for l in open("day_15.txt","r"):
    X=re.search(r"\D*x=(-?\d*), y=(-?\d*)\D*x=(-?\d*), y=(-?\d*)",l)
    x0,y0,x1,y1=(int(X.group(k)) for k in range(1,5))
    scan[(x0,y0)]=(x1,y1)
    dist[(x0,y0)]=abs(x1-x0)+abs(y1-y0)


def row_eligible(yt):
    bad=[]
    for k in scan.keys():
        dy=abs(yt-k[1])
        d=dist[k]-dy
        if d<0: continue
        a1,b1=k[0]-d,k[0]+d
        add=True

        i=0
        while i < len(bad):
            a2,b2=bad[i]

            if a1>b2 or a2>b1: 
                i+=1
                continue

            if a2<=a1 and b2>=b1:
                add = False
                break
                
            if a1<=a2 and b1>=b2:
                bad.pop(i)
                continue

            ai,bi=max(a1,a2),min(b1,b2)

            if a2 == ai:
                bad[i]=(bi+1,b2)
                i+=1
                continue

            if b2 == bi:
                bad[i]=(a2,ai-1)
                i+=1
                continue

            bad.pop(i)
            bad.insert((a2,ai-1),0)
            bad.insert((bi+1,b2),0)
            i+=2

        if add: bad.append((a1,b1))
    
    bad=sorted(bad,key=lambda x: x[0])
    for k in range(len(bad)-1):
        if not bad[k+1][0] == bad[k][1]+1:
            if 0<=bad[k][1]+1<=MAX:
                return bad[k][1]+1
    
    return None

for y in range(0,MAX+1):
    x=row_eligible(y)
    if not x == None:
        print(x,y)
        print(4000000*x+y)
        break




