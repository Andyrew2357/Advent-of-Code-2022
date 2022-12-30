O=set()
E={}

ind=0
for r,l in enumerate(open("day_23.txt")):
    for c,ch in enumerate(l):
        if ch=="#": 
            ind+=1
            O.add((r,c))
            E[ind]=(r,c,-1)


dr=[-1,1,0,0]
dc=[0,0,-1,1]

def cleared(r,c,d):
    match d:
        case 0: return {(r-1,c),(r-1,c-1),(r-1,c+1)}
        case 1: return {(r+1,c),(r+1,c-1),(r+1,c+1)}
        case 2: return {(r,c-1),(r-1,c-1),(r+1,c-1)}
        case 3: return {(r,c+1),(r-1,c+1),(r+1,c+1)}

def neighbors(r,c):
    return {(r+1,c),(r-1,c),(r,c+1),(r,c-1), (r+1,c+1),(r+1,c-1),(r-1,c+1),(r-1,c-1)}

NUM_IT=10000
new=set()
contest=set()
pref=0

for it in range(NUM_IT):
    for e in E:
        r,c,_=E[e]

        if not neighbors(r,c) & O:
            E[e]=(r,c,-1)
            continue

        d=-1
        for d_ in range(4):
            if not cleared(r,c,(pref+d_)%4) & O:
                d=(pref+d_)%4
                break

        if d==-1:
            E[e]=(r,c,-1)
            continue

        new_loc=(r+dr[d],c+dc[d])

        if new_loc in contest:
            E[e]=(r,c,-1)
            continue

        if new_loc in new:
            new.remove(new_loc)
            contest.add(new_loc)
            E[e]=(r,c,-1)
            continue

        new.add(new_loc)
        E[e]=(r,c,d)

    if len(new)==0: 
        print("part2: ", it+1)
        break

    for e in E:
        r,c,d=E[e]
        if d<0:continue
        new_r,new_c=r+dr[d],c+dc[d]
        if (new_r,new_c) in contest: continue
        O.remove((r,c))
        E[e]=(new_r,new_c,-1)
    
    O.update(new)

    new.clear()
    contest.clear()
    pref=(pref+1)%4

    print(it,": ",len(O))

# PART 1: Set NUM_IT to 10 and uncomment these

# rows=[r for (r,c) in O]
# cols=[c for (r,c) in O]

# h,w=1+max(rows)-min(rows),1+max(cols)-min(cols)

# print("part1: ", w*h-len(O))
# print(w,h)