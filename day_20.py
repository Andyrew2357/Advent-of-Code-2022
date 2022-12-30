inst=[]
lst=[]
ENCRYPTION_KEY=811589153

for k,l in enumerate(open("day_20.txt","r")):
    n=int(l.strip())*ENCRYPTION_KEY
    inst.append(n)
    lst.append((n,k))
    if n==0:
        zero=(0,k)

#print(lst)
m=len(inst)

NUM_MIXES=10
for _ in range(NUM_MIXES):
    for k,cmd in enumerate(inst):
        in_=cmd,k

        if cmd%(m-1)==0: continue

        #print(cmd)
        
        st=lst.index(in_)
        lst.pop(st)
        en=(st+cmd)%(m-1)
        lst.insert(en,(cmd,k))

        #print(lst)

ind=lst.index(zero)
print(lst[(ind+1000)%m][0],"+",lst[(ind+2000)%m][0],"+",lst[(ind+3000)%m][0],"=",lst[(ind+1000)%m][0]+lst[(ind+2000)%m][0]+lst[(ind+3000)%m][0])

