from collections import deque

t={"=":-2,"-":-1,"0":0,"1":1,"2":2}

tot=0
for l in open("day_25.txt","r"):
    num=0
    for k,ch in enumerate(l.strip()[::-1]):
        num+=(5**k)*t[ch]
    tot+=num

print("base 10: ",tot)

tinv={0:"0",1:"1",2:"2",3:"=",4:"-"}

new_base=deque([])

place_ex=0
while tot>0:
    r=tot%5
    tot=tot//5
    new_char=tinv[place_ex+r]

    new_base.appendleft(new_char)

    if new_char in ["=","-"]:
        place_ex=1
    else:
        place_ex=0

print("part1: ","".join(new_base))
    

