import time

start_t=time.perf_counter()

# states represented by
# (stockpile:ore,clay,obsidian,geode, robots:ore,clay,obsidian,geode)
SEEN={}

def geodes_produced(state):
    if len(SEEN)%100000==0:print(len(SEEN))

    time,Or,Cl,Ob,Ge,Or_r,Cl_r,Ob_r,Ge_r=state
    if time==1: return Ge+Ge_r

    no_Or,no_Cl,no_Ob=False,False,False
    if Or >= time*max(cost["Ge"][0],cost["Ob"][0],cost["Cl"],cost["Or"]):
        Or=time*max(cost["Ge"][0],cost["Ob"][0],cost["Cl"],cost["Or"])
        Or_r=0
        no_Or=True
    if Cl >= time*cost["Ob"][1]:
        Cl=time*cost["Ob"][1]
        Cl_r=0
        no_Cl=True
    if Ob >= time*cost["Ge"][1]:
        Ob=time*cost["Ge"][1]
        Ob_r=0
        no_Ob=True

    if Or_r >= max(cost["Ge"][0],cost["Ob"][0],cost["Cl"],cost["Or"]) and Or>= max(cost["Ge"][0],cost["Ob"][0],cost["Cl"],cost["Or"]):
        Or=time*max(cost["Ge"][0],cost["Ob"][0],cost["Cl"],cost["Or"])
        Or_r=0
        no_Or=True
    
    if Cl_r >= cost["Ob"][1] and Cl >= cost["Ob"][1]:
        Cl=time*cost["Ob"][1]
        Cl_r=0
        no_Cl=True

    if Ob_r >= cost["Ge"][1] and Ob >= cost["Ge"][1]:
        Ob=time*cost["Ge"][1]
        Ob_r=0
        no_Ob=True
    
    state=(time,Or,Cl,Ob,Ge,Or_r,Cl_r,Ob_r,Ge_r)

    if state in SEEN: return SEEN[state]

    new_Or,new_Cl,new_Ob,new_Ge=Or+Or_r,Cl+Cl_r,Ob+Ob_r,Ge+Ge_r

    # I think that if you can make a geode robot it is always best to.
    if Or>=cost["Ge"][0] and Ob>=cost["Ge"][1]:
        ans=geodes_produced((time-1,new_Or-cost["Ge"][0],new_Cl,new_Ob-cost["Ge"][1],new_Ge,Or_r,Cl_r,Ob_r,Ge_r+1))
        SEEN[state]=ans
        return ans

    ans=geodes_produced((time-1,new_Or,new_Cl,new_Ob,new_Ge,Or_r,Cl_r,Ob_r,Ge_r))

    if not no_Ob and Or>=cost["Ob"][0] and Cl>=cost["Ob"][1]:
        ans=max(ans,geodes_produced((time-1,new_Or-cost["Ob"][0],new_Cl-cost["Ob"][1],new_Ob,new_Ge,Or_r,Cl_r,Ob_r+1,Ge_r)))

    if not no_Cl and Or>=cost["Cl"]:
        ans=max(ans,geodes_produced((time-1,new_Or-cost["Cl"],new_Cl,new_Ob,new_Ge,Or_r,Cl_r+1,Ob_r,Ge_r)))

    if not no_Or and Or>=cost["Or"]:
        ans=max(ans,geodes_produced((time-1,new_Or-cost["Or"],new_Cl,new_Ob,new_Ge,Or_r+1,Cl_r,Ob_r,Ge_r)))

    SEEN[state]=ans
    return ans


tot=0
res=[]
for i,l in enumerate(open("day_19.txt","r")):
    #PART 2
    if i>2: break

    blue=l.strip().split()
    cost={}

    # ore
    cost["Or"]=int(blue[6])
    # ore
    cost["Cl"]=int(blue[12])
    # ore, clay
    cost["Ob"]=(int(blue[18]),int(blue[21]))
    # ore, obsidian
    cost["Ge"]=(int(blue[27]),int(blue[30]))

    SEEN.clear()

    # ans=geodes_produced((24,0,0,0,0,1,0,0,0))
    # tot+=ans*(i+1)
    # print(ans,tot)

    ans=geodes_produced((32,0,0,0,0,1,0,0,0))
    print(ans)
    res.append(ans)

print(tot)
print(res)
print(res[0]*res[1]*res[2])

print("time: ", time.perf_counter()-start_t)