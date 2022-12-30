trans={"A":0,"B":1,"C":2,"X":0,"Y":1,"Z":2}
score=0
score2=0
with open("day_2_input.txt") as f:

    for l in f.readlines():
        x=l[0:1]
        y=l[2:3]
        score+=trans[y]+1
        if trans[y]%3 == (trans[x]+1)%3:
            score+=6
        elif trans[x]==trans[y]:
            score+=3
        
        if y=="Y":
            score2+=3
            score2+=trans[x]+1
        elif y=="Z":
            score2+=6
            score2+=(trans[x]+1)%3+1
        else:
            score2+=(trans[x]-1)%3+1


print(score)
print(score2)
