import numpy as np

with open("day_8.txt","r") as f:
    l=f.readlines()
    trees=np.zeros(shape=(len(l),len(l[0].strip())))
    m,n=trees.shape
    for r,s in enumerate(l):
        trees[r,:]=[int(c) for c in s.strip()]

tot=2*(m+n-2)

for r in range(1,n-1):
    for c in range(1,m-1):
        l_max=np.amax(trees[r,:c])
        r_max=np.amax(trees[r,c+1:])
        u_max=np.amax(trees[:r,c])
        d_max=np.amax(trees[r+1:,c])
        min_cover=min(l_max,r_max,u_max,d_max)
        if trees[r,c]>min_cover:
            tot+=1
print(tot)

best_view=0
for r in range(1,m-1):
    for c in range(1,n-1):
        left=0
        for lv in range(c-1,0,-1):
            if trees[r,c]<=trees[r,lv]:
                left=lv
                break
        right=n-1
        for rv in range(c+1,n):
            if trees[r,c]<=trees[r,rv]:
                right=rv
                break
        up=0
        for uv in range(r-1,0,-1):
            if trees[r,c]<=trees[uv,c]:
                up=uv
                break
        down=m-1
        for dv in range(r+1,m):
            if trees[r,c]<=trees[dv,c]:
                down=dv
                break
        view=(c-left)*(right-c)*(r-up)*(down-r)
        if view>best_view:
            # print(r,c,":",(c-left),(right-c),(r-up),(down-r))
            best_view=view

print(best_view)