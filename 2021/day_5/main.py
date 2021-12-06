import re
import numpy as np

filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] #Reads the file and strips trailing whitespaces newlines etc, cleaner solution of inputting file than before.

def get_max(input):
    (xmax, ymax) = 0, 0
    for line in input:
        (x1, y1, x2, y2) = [int(x) for x in re.findall('\d+', line)]
        if x1 > xmax or x2 > xmax:
            xmax = max(x1, x2)
        if y1 > ymax or y2 > ymax:
            ymax = max(y1, y2)
    return xmax, ymax

def solution_1(input):
    for line in input:
        (x1, y1, x2, y2) = [int(x) for x in re.findall('\d+', line)]

        #X or Y is going to match if only matching straight lines
        if x1 == x2:
            minY = min(y1, y2)
            maxY = max(y1, y2)
            numpy_table[minY:maxY+1, x1] += 1
        elif y1 == y2:
            minX = min(x1, x2)
            maxX = max(x1, x2)
            numpy_table[y1, minX:maxX+1] += 1
    return len(numpy_table[numpy_table > 1])

def solution_2(input):
    for line in input:
        (x1, y1, x2, y2) = [int(x) for x in re.findall('\d+', line)]

        #We only need to run this if the original x and y values don't match up, we've already got the straight lines from part 1's solution.
        if x1 != x2 and y1 != y2:
            minX = min(x1, x2)
            maxX = max(x1, x2)
            minY = min(y1, y2)
            maxY = max(y1, y2)
            #Calculate how many fields we need to alter.
            steps = (maxX - minX)+1
            #The difference between both X and Y should be equal, if they are not something is wrong with our input data.
            if steps != (maxY-minY)+1:
                print("Steps don't match something's wrong with the data.")
            #For every step we mark the spot on the floor that corresponds with x and y.
            
            for _ in range(steps):
                numpy_table[y1, x1] += 1
                #Find out in what direction we want to move.
                x1 -= 1 if x1 > x2 else -1
                y1 -= 1 if y1 > y2 else -1
    return len(numpy_table[numpy_table > 1])

(xmax, ymax) = get_max(input) #Fill these variables with values from our input.
numpy_table = np.zeros((ymax+1, xmax+1)) #We create a table filled with 0's that corresponds to the ocean floor based on the max y and x values given to us.
answer1 = solution_1(input)
#For part 2 we are keeping the data from part 1 and adding onto it.
answer2 = solution_2(input)

print('Without diagonals there are', answer1 ,'spots that are overlapping')
print('With diagonals there are', answer2 ,'spots that are overlapping')