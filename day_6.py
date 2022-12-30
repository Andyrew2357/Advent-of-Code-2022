
with open("day_6.txt","r") as f:
    l=f.readline()
    for k in range(14,len(l)):
        s=l[k-14:k]
        good=True
        for i in range(13):
            c=s[i]
            if c in s[i+1:]:
                good=False
        if good:
            print(k)
            break
