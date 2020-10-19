import random
from random import choice
density=0.2 #random.random()
maxsteps=10000#00
npart=500 #500
side=21  #21Should be an odd number
perc=0

steps = [(1, 0), (-1, 0), (0, 1), (0,- 1)]
grid=[[0 for x in range(side)] for y in range(side)]
for ipart in range(npart):#running npart # of trials
    # fill matrix
    for x in range(side):
        for y in range(side):
            fill = random.random()
            if(fill < density):
                grid[x][y]=1
    # Start particle at center
    x,y = side//2,side//2
    # perform the random walk until particle departs
    for i in range(maxsteps):
        grid[x][y] = 0   #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        print(x,y)
        if grid[x][y]==1:#checking if cell is occupied or not
            x -= sx
            y -= sy
            continue
        if x<0 or y<0 or x==side or y==side:
            perc+=1
            break



        grid[x][y]=1   #Put particle in new location
print("probability of percolation:", perc/npart)



