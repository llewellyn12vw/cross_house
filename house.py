import matplotlib.pyplot as plt
import time
import copy
import numpy as np
import matplotlib.animation as animation

coordinates = {1: (1,1), 2: (1,3), 3: (2,5), 4: (3,3), 5: (3,1)}
combinations = {1: [2,4,5], 2: [1,3,4,5], 3: [2,4], 4: [1,2,3,5], 5: [1,2,4]}
house = list()
total = list()

def tree(a,b):  
    if((a,b) in house or (b,a) in house):
        if(len(house)!=8):
            return False
    else: house.append((a,b)) 
    
    if(len(house)==8): 
        d = copy.deepcopy(house)
        total.append(d)
        house.pop()
        return 
    
    new_a = b  
    for z in combinations[b]:
        if(z == a): continue
        l = tree(new_a,z)
        if l == False:  
            continue
    house.pop()   
    return 


for i in combinations.keys():
    for j in combinations[i]:
        tree(i,j)

print(len(total), 'different configurations to draw a cross house')

def data_gen():
    first = 0
    for i in total:
        for j in i:
            for k in j:
                if(i.index(j)==0 and j.index(k)==0):
                    first = 1
                else: first = 0
                x = coordinates[k][0]
                y = coordinates[k][1]                
                yield x,y, first


def init():
    ax.set_ylim(0, 5)
    ax.set_xlim(0, 4)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    x, y, start = data
    if(start == 1):
        xdata.clear()
        ydata.clear()
    
    xdata.append(x)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    line.set_data(xdata, ydata)
    return line,

# Only save last 100 frames, but run forever
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
plt.show()
        
