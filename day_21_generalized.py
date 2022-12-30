monkeys={}

for l in open("day_21.txt","r"):
    d=l.strip().split()
    key=d[0][0:-1]
    if len(d)==2:
        val=int(d[1])
    else:
        val=tuple(d[1:])

    monkeys[key]=val

def monkey_v(name):
    match monkeys[name]:
        case a,"+",b: return monkey_v(a) + monkey_v(b)
        case a,"*",b: return monkey_v(a) * monkey_v(b)
        case a,"-",b: return monkey_v(a) - monkey_v(b)
        case a,"/",b: return monkey_v(a) / monkey_v(b)
        case x: return x

print("part1: ",monkey_v("root"))

# THE WAY THESE INPUTS ARE STRUCTURED, "cwtl" is linear in f

m1,_,m2= monkeys["root"]

monkeys["humn"]=0

b1=monkey_v(m1)
b2=monkey_v(m2)

monkeys["humn"]=1e7

a1=(monkey_v(m1)-b1)/1e7
a2=(monkey_v(m2)-b2)/1e7

guess=int((b2-b1)/(a1-a2))
print("correct p2 using my initial method: ",3247317268284)
print("initial guess using intersection: ", guess)

# I'm going to use bisection to find the solution given this linear guess

lower=guess-int(1e3)
upper=guess+int(1e3)
monkeys["humn"]=lower
yl=monkey_v(m1)-monkey_v(m2)
monkeys["humn"]=upper
yu=monkey_v(m1)-monkey_v(m2)


for _ in range(20):
    xm=(upper+lower)//2
    monkeys["humn"]=xm
    ym=monkey_v(m1)-monkey_v(m2)
    if ym==0:
        print("part2 ans: ",monkeys["humn"])
        break
    if yl*ym < 0:
        upper=xm
        yu=ym
    else:
        lower=xm
        yl=ym

