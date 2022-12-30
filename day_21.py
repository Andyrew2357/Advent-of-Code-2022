monkeys={}

for l in open("day_21.txt","r"):
    d=l.strip().split()
    key=d[0][0:-1]
    if len(d)==2:
        val=int(d[1])
    else:
        val=tuple(d[1:])

    monkeys[key]=val

dependency={}
def monkey_v(name):
    if type(monkeys[name])==tuple:
        for n in monkeys[name]:
            dependency[n]=name
    match monkeys[name]:
        case a,"+",b: return monkey_v(a) + monkey_v(b)
        case a,"*",b: return monkey_v(a) * monkey_v(b)
        case a,"-",b: return monkey_v(a) - monkey_v(b)
        case a,"/",b: return monkey_v(a) / monkey_v(b)
        case x: return x

print("part1: ",monkey_v("root"))


# cwtl NEEDS INPUT FROM humn, BUT wqpn DOESN'T

print("target: ",monkey_v("wqpn"))

# "humn" only gets used by "lptd", which is used by "jcmb", etc. I should automate this process

dep_arr=["humn"]

loc="humn"
while not loc=="root":
    new_loc=dependency[loc]
    dep_arr.append(new_loc)
    loc=new_loc

dep_arr.pop()
print(dep_arr)

expression=""

for k in range(len(dep_arr)):
    cur=dep_arr[k]

    if cur=="humn":
        expression="x"
        continue

    deps=monkeys[cur]

    right=(deps[0]==dep_arr[k-1])

    if right:
        expression="("+expression+")"+deps[1]+str(monkey_v(deps[2]))
    else:
        expression=str(monkey_v(deps[0]))+deps[1]+"("+expression+")"

print("expression: ",expression)

# THIS GIVES ME A GROSS LOOKING EXPRESSION THAT I'LL JUST SIMPLIFY IN WOLFRAM ALPHA OR SOMETHING

# According to this website (https://www.mathpapa.com/simplify-calculator/), this simplifies to

#-(160/9)x + 340883953559596/3 = target = 55897899750372

# I now just do the algebra in terminal

# This gives me 3247317268284 for my input. Don't ask me to do this for anyone else's input though. That sounds like a hassle.
