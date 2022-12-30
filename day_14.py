
filled=set()

# parsing input
bottom=0
for l in open("day_14.txt","r"):
    vert=l.strip().split(" -> ")

    x0,y0=(int(s) for s in vert[0].split(","))
    if y0>bottom: bottom=y0

    for k in range(1, len(vert)):
        x1,y1=(int(s) for s in vert[k].split(","))
        if y1>bottom: bottom=y1

        if x0==x1:
            for y in range(min(y0,y1),max(y0,y1)+1):
                filled.add((x0,y))
        else:
            for x in range(min(x0,x1),max(x0,x1)+1):
                filled.add((x,y0))

        x0,y0=x1,y1

# import numpy as np

# board=np.zeros(shape=(150,200))
# for r in range(150):
#     for c in range(200):
#         if (r+400,c) in filled:
#             board[r,c]+=1

xs,ys=500,0
tot=0

while True:
    x,y=xs,ys

    while True:
        #if y>bottom: break
        if y==bottom+1:
            break

        if not (x,y+1) in filled:
            y+=1
        elif not (x-1,y+1) in filled:
            x-=1
            y+=1
        elif not (x+1,y+1) in filled:
            x+=1
            y+=1
        else:
            break
    
    #if y>bottom: break
    tot+=1
    if y==0:break
    filled.add((x,y))

print(tot)

# for r in range(150):
#     for c in range(200):
#         if (r+400,c) in filled:
#             board[r,c]+=1

# from matplotlib import pyplot as plt

# plt.imshow(np.transpose(board))
# plt.show()