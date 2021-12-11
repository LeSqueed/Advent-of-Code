#Solve 1, count number of flashes after 100 steps.
#Idea:
#Step 1: Set every value above 9 to 0, this has flashed in the previous step.
#Step 2: Increase everything with 1.
#Step 2: Start a while loop, while there is a 9 in the array keep looping.
#Step 3: During the while loop, find all 9's and increase their neigbours by one, increase counter by one, and after that increase it's own value by one. Don't worry about resetting it to 0 here, we can do that again on the start of our next step.
#Warnings: If neighbour is 9, do NOT increase it by one, we will still get to this one later. Check if you are in the first or last row/column since some neighbours will be out of range.

#Neighbours are:
#Row+1 straight
#Row-1 straight
#Column+1 straight
#Column-1 straight
#Row+1, Column+1 diagonal
#Row+1, Column-1 diagonal
#Row-1, Column+1 diagonal
#Row-1, Column-1 diagonal

import numpy as np
filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 


#Get dimensions needed for our arrays
R = sum(1 for _ in input)
C = len(input[1].rstrip())

#How many steps we to generate.
steps = 100

def fill_map(input):
    #Enumerate line for row number and position in that row for the column number.
    squid_map = np.empty([R,C], dtype=int)
    for line, data in enumerate(input):
        for pos, nr in enumerate(data):
            squid_map[line, pos] = nr
    return squid_map

def solve_1(input):
    #Our counter for the amount of flashes
    flashes = 0
    squid_map = fill_map(input)
    #Repeat for X amount of steps
    for _ in range(steps+1):
        #Add one to every row to get things started
        #Count all 0's so we get the flashes that happened. 
        flashes += squid_map.size - np.count_nonzero(squid_map)
        squid_map += 1
        while(np.any(squid_map >= 10)):
            for index, number in np.ndenumerate(squid_map):
                left = max(0, index[0]-1)
                right = max(0, index[0]+2)
                top =  max(0, index[1]+2)
                bottom = max(0, index[1]-1)

                #Segment with all neighbours, +1 if current number is 9. 
                if number >= 10:     
                    squid_map[left:right, bottom:top] = np.where(squid_map[left:right, bottom:top] > 0, squid_map[left:right, bottom:top]+1, squid_map[left:right, bottom:top])
                    squid_map[index] = 0
    return flashes

def solve_2(input):
    #Our counter for which step we are on.
    step = 0
    squid_map = fill_map(input)
    synchronized = False
    #Repeat for X amount of steps
    while(synchronized == False):
        #Add one to every row to get things started
        #When there are only 0's we are done. 
        synchronized = True if squid_map.size - np.count_nonzero(squid_map) == squid_map.size else False
        step +=1
        squid_map += 1
        while(np.any(squid_map >= 10)):
            for index, number in np.ndenumerate(squid_map):
                left = max(0, index[0]-1)
                right = max(0, index[0]+2)
                top =  max(0, index[1]+2)
                bottom = max(0, index[1]-1)

                #Segment with all neighbours, +1 if current number is 9. 
                if number >= 10:     
                    squid_map[left:right, bottom:top] = np.where(squid_map[left:right, bottom:top] > 0, squid_map[left:right, bottom:top]+1, squid_map[left:right, bottom:top])
                    squid_map[index] = 0
    #Subtract one since we've also counted the initial state in our steps.
    return step-1

print('We got',solve_1(input), 'flashes.')

print('It took', solve_2(input), 'steps to sync them up.')