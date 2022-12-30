# We Need to Make Use of Repeated Patterns.
# We'll keep a dictionary for patterns consisting of the last 30 or so lines in the tower.
# I don't like this solution. To my mind we haven't fully justified why a piece could never
# wind up falling totally past this pattern, but if it works, it works.

with open("day_17.txt","r") as f:
    wind=f.readline().strip()
    windl=len(wind)

# BLOCK INFORMATION
b_blocks={
    0:((0,0),(1,0),(2,0),(3,0)),
    1:((1,0),(0,1),(1,1),(2,1),(1,2)),
    2:((0,0),(1,0),(2,0),(2,1),(2,2)),
    3:((0,0),(0,1),(0,2),(0,3)),
    4:((0,0),(1,0),(0,1),(1,1))
}

b_bottom={
    0:((0,0),(1,0),(2,0),(3,0)),
    1:((1,0),(0,1),(2,1)),
    2:((0,0),(1,0),(2,0)),
    3:((0,0),),
    4:((0,0),(1,0))
}

b_left={
    0:((0,0),),
    1:((0,1),(1,0),(1,2)),
    2:((0,0),(2,1),(2,2)),
    3:((0,0),(0,1),(0,2),(0,3)),
    4:((0,0),(0,1))
}

b_right={
    0:(3,((3,0),)),
    1:(2,((2,1),(1,0),(1,2))),
    2:(2,((2,0),(2,1),(2,2))),
    3:(0,((0,0),(0,1),(0,2),(0,3))),
    4:(1,((1,0),(1,1)))
}


tower=set([(k,0) for k in range(7)])
SEEN={}
SAVED_ROWS=30

def tower_top():
    tow_top=max([y for (x,y) in tower])
    return frozenset([(x,tow_top-y) for (x,y) in tower if tow_top-y<=SAVED_ROWS])

TOTAL_BLOCKS=1000000000000
blocks_dropped=0
wind_time=0
top=0

while blocks_dropped<TOTAL_BLOCKS:
    block=b_blocks[blocks_dropped%5]
    bottom=b_bottom[blocks_dropped%5]
    left=b_left[blocks_dropped%5]
    max_r,right=b_right[blocks_dropped%5]
    tow_top=max([y for (x,y) in tower])

    x,y=2,tow_top+4
    blocks_dropped+=1

    while True:
        wind_pattern=wind[wind_time]
        wind_time=(wind_time+1)%windl

        if wind_pattern=="<" and x>0:
            can_move=True
            for dx,dy in left:
                if (x+dx-1, y+dy) in tower:
                    can_move=False
                    break
            if can_move: x-=1
        elif wind_pattern==">" and x+max_r<6:
            can_move=True
            for dx,dy in right:
                if (x+dx+1, y+dy) in tower:
                    can_move=False
                    break
            if can_move: x+=1
        
        Falling=True
        for dx,dy in bottom:
            if (x+dx,y+dy-1) in tower:
                Falling=False
                above=0
                for x_,y_ in block:
                    tower.add((x+x_,y+y_))
                    above=max(above,y+y_-tow_top)
                top+=above
                break
        y-=1
        
        if not Falling:
            KEY=tower_top()
            if KEY in SEEN:
                prev_blocks,prev_top=SEEN[KEY]
                repetition_height=top-prev_top
                repetition_blocks=blocks_dropped-prev_blocks
                amt=(TOTAL_BLOCKS-blocks_dropped)//repetition_blocks
                top+=amt*repetition_height
                blocks_dropped+=amt*repetition_blocks
            if tow_top>=SAVED_ROWS: SEEN[KEY]=blocks_dropped,top
            break

print(top)


# NOTES

# If it's already seen the last 30 lines of the tower repeated before, it assumes those will repeat for as long as they can without 
# exceeding the number of blocks. I don't think this is rigorous. I think you have to do a little more work to make it work, and there 
# may be pathological inputs where this fails. You can probably show this works if you make SAVED_ROWS sufficiently large compared to 
# the wind pattern or something, but I just gave a guess at 30 that seems like it works.
# For reference, if I give it 28, then it fails
# it needs 29 or above for my input
# the example they give in the problem needs 10
# They must have had a more rigorous way of validating their puzzles, like somehow forcing the crevices on either side of the tower to close 
# off sufficiently often and properly accounting for the periodicity of the input relative to the blocks.
# I noticed that the length of my input was a prime number 1091, but I don't know if that's integral to the way they generate them.
# My initial thought, the dream scenario, would have been to look for a number of iterations that left you with a full row filled. 
# That would allow me to do this completely rigorously, but I guess if it works it works.