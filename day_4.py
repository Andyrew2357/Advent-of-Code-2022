tot=0
tot2=0
with open("day_4.txt","r") as f:
    for line in f:
        x1,x2=line.split(",")
        x1=x1.split("-")
        x2=x2.split("-")
        x1=[int(x) for x in x1]
        x2=[int(x) for x in x2]
        if (x1[0]<=x2[0] and x2[1]<=x1[1]) or (x2[0]<=x1[0] and x1[1]<=x2[1]):
            tot+=1
        if (x1[0]<=x2[1] and x1[1]>=x2[0]) or (x2[0]<=x1[1] and x2[1]>=x1[0]):
            tot2+=1

print(tot)
print(tot2)