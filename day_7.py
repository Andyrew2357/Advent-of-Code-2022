d={}

with open("day_7.txt") as f:
    cd="/"
    ls=[]
    for line in f:
        l=line.strip()
        if l[0]=="$":
            if l[0:5] == "$ cd ":
                
                if not len(ls) == 0:
                    d[cd]=tuple(ls)
                ls=[]

                opt=l.split()[2]
                if opt == "/":
                    cd="/"
                elif opt == "..":
                    cd=cd[0:cd[0:-2].rindex("/")+1]
                else:
                    cd+=(opt+"/")
            continue
        ls.append(l)
    if not len(ls)==0:
        d[cd]=tuple(ls)

print(d["/"])

def tot_size(dir):
    total=0
    if not dir in d.keys():
        return 0
    for sub in d[dir]:
        if sub[0]=="d":
            total+=tot_size(dir+sub.split()[1]+"/")
        else:
            total+=int(sub.split()[0])
    return total

tot=0
target=30000000-(70000000-tot_size("/"))
print("target: ",target)
min_eligible=10000000000000000

for k in d.keys():
    s=tot_size(k)
    if s<=100000:
        tot+=s
    if s>=target and s<min_eligible:
        min_eligible=s
    # if s >= target:
    #     print(s)

print(tot)
print(min_eligible)
