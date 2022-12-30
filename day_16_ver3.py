import re
from collections import defaultdict
from collections import deque

connections={}
flow_rate={}
ind={}

i=0
for l in open("day_16t.txt","r"):
    d=re.match(r"Valve (\w\w) has flow rate=(\d*); tunnel\w? lead\w? to valve\w? (.*)",l)
    node=d.group(1)
    rate=d.group(2)
    conn=tuple(d.group(3).split(", "))

    connections[node]=conn
    flow_rate[node]=int(rate)
    ind[node]=i
    i+=1

num_valves=i

# My intuition that the problem with multiple people is the same as if you 
# did it optimally with one person and then did it for each subsequent person
# with the valves that were previously opened removed.

TIME=26
seen={}

def max_pressure(x,openV,time,players):

    if time == 1: return 0 if players == 1 else max_pressure('AA',openV,TIME,players-1)

    id_=(x,openV,time,players)
    if id_ in seen: return seen[id_]

    ans=0

    for n in connections[x]:
        ans=max(ans,max_pressure(n,openV,time-1,players))

    if openV[ind[x]] == "0" and flow_rate[x] > 0:
        new_openV = openV[:ind[x]]+"1"+openV[ind[x]+1:]
        ans=max(ans,max_pressure(x,new_openV,time-1,players)+(time-1)*flow_rate[x])
    
    seen[id_]=ans
    return ans

pressure=max_pressure('AA',str("0"*num_valves),TIME,2)
print(pressure)

# There are most certainly optimizations to be made with this dictionary and the keys
# I also expect that there might be some amount of superfluous computation going on.

# The trick of having players go one after another is more subtle than people might realize.
# After finishing this, I now realize my statement for the intuition at the top is actually
# wrong. You aren't solving for the optimal path given just the first player. You solve for
# the optimal first path subject to the restriction that there is a second player, which is 
# very different and the only reason why this approach works in the first place. I assume this
# is also why the second part still takes much longer than the first. The complexity is not
# at all linear.