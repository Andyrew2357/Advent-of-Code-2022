import ast

def compare(arr1,arr2):
    for k in range(min(len(arr1),len(arr2))):
        a1=arr1[k]
        a2=arr2[k]

        if type(a1)==int and type(a2)==int:
            if a1<a2: return True
            if a1>a2: return False
            continue

        if type(a1)==list and type(a2)==list:
            comp=compare(a1,a2)
            if comp==None: continue
            return comp

        if type(a1)==int: 
            a1=[a1]
        else:
            a2=[a2]
        
        comp=compare(a1,a2)
        if comp==None: continue
        return comp

    if len(arr1)<len(arr2): return True
    if len(arr1)>len(arr2): return False
    return None

with open("day_13.txt","r") as f:
    l=f.readlines()
    l=[s.strip() for s in l]

tot=0
for k in range(0,len(l),3):
    a1=ast.literal_eval(l[k])
    a2=ast.literal_eval(l[k+1])

    if compare(a1,a2): 
        tot+=(k//3)+1

print("part1: ",tot)

# Being more clever for part 2, I think I can try to give a numerical value to the arrays representing their "score" per say.
# There are some bugs that make it so this doesn't always properly map on to the comparisons, but it's close, and it only disagrees 
# with my comparison function for 2 or 3 of the inputs. For that reason, I'll use it as a heuristic to do most of the sorting and then
# do the rest of the slow sorting with the comparison function.

def convert(arr):
    if len(arr)==0: return 1.
    base=30
    tot=0.
    for k,a in enumerate(arr):
        if type(a)==int:
            tot+=(base**(-k))*(a+2)
        else:
            tot+=(base**(-k))*convert(a)
    return tot

lines=[]
scores=[]
for k in range(0,len(l),3):
    a1=ast.literal_eval(l[k])
    a2=ast.literal_eval(l[k+1])
    
    lines.append(a1)
    lines.append(a2)

    scores.append(convert(a1))
    scores.append(convert(a2))

lines.append([[2]])
scores.append(convert([[2]]))
lines.append([[6]])
scores.append(convert([[6]]))

lines=[l for l,v, in sorted(zip(lines,scores), key=lambda x:x[1])]


print("_________________")
print("Heuristic Guess:")
print("[[2]]: ", lines.index([[2]]))
print("[[6]]: ", lines.index([[6]]))
print("_________________")

import functools

def comparison(a1,a2):
    comp=compare(a1,a2)
    if comp==None:return 0
    if comp: 
        return -1 
    else: 
        return 1

lines=sorted(lines,key=functools.cmp_to_key(comparison))

print("_________________")
print("Refined:")
print("[[2]]: ", lines.index([[2]]))
print("[[6]]: ", lines.index([[6]]))
print("_________________")

print("part 2: ",(lines.index([[2]])+1)*(lines.index([[6]])+1))