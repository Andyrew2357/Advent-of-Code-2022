
import numpy as np
vals=np.zeros(240,dtype=int)

with open("day_10.txt","r") as f:
    ind=0
    x=1

    while ind < 240:
        cmd=f.readline().strip().split()
        if len(cmd)==1: 
            vals[ind]=x
            ind+=1
        else:
            vals[ind]=x
            vals[ind+1]=x
            ind+=2
            x+=int(cmd[1])


print(sum([(i+1)*vals[i] for i in range(19,220,40)]))

screen=np.zeros(240,dtype=int)

for i in range(240):
    if abs(vals[i]-i%40)<=1:
        screen[i]=1

from matplotlib import pyplot as plt

plt.imshow(screen.reshape((6,40)))
plt.show()
            