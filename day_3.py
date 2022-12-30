import time

start=time.perf_counter()
priority="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

tot=0
tot2=0
with open("day_3_input.txt","r") as f:
    lines=f.readlines()

    for i in range(0,len(lines),3):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                tot2+=priority.index(c)+1
                break  

    for l in lines:
        s1,s2=l[0:len(l)//2],l[len(l)//2:len(l)-1]
        for c in s1:
            if c in s2:
                tot+=priority.index(c)+1
                break
    
print(tot)
print(tot2)
print(time.perf_counter()-start)