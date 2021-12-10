import numpy as np

filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 

#Find low points. Values that are the lowest value compared to their neighbours in a straight line.
#Risk level of low points is value+1.
#Solve 1 is sum of risk level of all low points.

#Thinking: Create a numpy table so we can check based on X and Y coordinates if it is the lowest point compared to it's neighbour.
#Might make two tables, one with values and one with the risk levels of each point. We can then at the end just sum the table at the end for total risk value.

#Get dimensions needed for our arrays
R = sum(1 for _ in input)
C = len(input[1].rstrip())

def fill_map(input):
    #Enumerate line for row number and position in that row for the column number.
    map = np.empty([R,C], dtype=int)
    for line, data in enumerate(input):
        for pos, nr in enumerate(data):
            map[line, pos] = nr
    return map

def gen_risk_values(map):
    map_risk_values = np.zeros([R, C], dtype=int)
    #Addition for part 2 a list of coordinates of known low points.
    low_points = []
    for index, number in np.ndenumerate(map):
        c_row = index[0]
        c_column = index[1]
        check_against = []
        #Figure out which values we need to check against, can't check outside of the map.
        if(c_row != 0):
            check_against.append(map[c_row-1, c_column])
        if(c_column != 0):
            check_against.append(map[c_row, c_column-1])
        if(c_row != R-1):
            check_against.append(map[c_row+1, c_column])
        if(c_column != C-1):
            check_against.append(map[c_row, c_column+1])
        if number < min(check_against):
            map_risk_values[c_row, c_column] += number+1
            #For part two also add the current position to a new list.
            low_points.append(index)
            #For everything else we check all neighbours
    return (map_risk_values, low_points)

#For part two, find the 3 largests basins. 
def find_basins(map, index):
    #Store all the sizes we find, we can later get the biggest 3 from here.
    basin_sizes = []

    #Iterate through each initial position that has a basin and store the end size in basin_sizes
    for i in index:
        i = [(i[0], i[1])]
        #let's create a new map (or if new run reset the map) with all 0's we can sum up later.
        map_basins = np.zeros([R, C], dtype=int)
        #Go through every basin in our index and map the size.
        searched = []
        #Keep going as long as there are coordinates in our i variable.
        while len(i) > 0:
            #We want to go through each row and column till we reach the end of the map or reach a 9 for every low position.
            #If we find a new row that's valid we also want to check every item in that column and vice versa for the column.
            #Avoid checking one location more than once for each basin.
            
            #Take first element in our i on our run and check if we've not searched it yet.
            if i[0] not in searched:
                searched.append(i[0])
                c_row = i[0][0]
                c_column = i[0][1]

                #Search rows in positive direction.
                while c_row >= 0:
                    #We want to look for values till we hit the edge or a 9.
                    if map[c_row, c_column] < 9:
                        map_basins[c_row, c_column] = 1
                        i.append((c_row, c_column))
                    else:
                        break
                    c_row -= 1

                c_row = i[0][0]
                c_column = i[0][1]

                #Searching rows in negative direction.
                while c_row <= R-1:
                    if map[c_row, c_column] < 9:
                        map_basins[c_row, c_column] = 1
                        i.append((c_row, c_column))
                    else:
                        break
                    c_row += 1

                c_row = i[0][0]
                c_column = i[0][1]

                #Searching columns in positive direction.
                while c_column >= 0:
                    #We want to look for values till we hit the edge or a 9.
                    if map[c_row, c_column] < 9:
                        map_basins[c_row, c_column] = 1
                        i.append((c_row, c_column))
                    else:
                        break
                    c_column -= 1
                
                c_row = i[0][0]
                c_column = i[0][1]

                #Searching columns in negative direction.
                while c_column <= C-1:
                    if map[c_row, c_column] < 9:
                        map_basins[c_row, c_column] = 1
                        i.append((c_row, c_column))
                    else:
                        break
                    c_column += 1

            #Remove current item from our i.
            i.pop(0)
        basin_sizes.append(map_basins.sum())
    #Sort the list by largest number so the largest 3 are always the ones at the front.
    basin_sizes.sort(reverse=True)

    #Return the largest numbers multiplied with each other.
    return basin_sizes[0]*basin_sizes[1]*basin_sizes[2]

#Generate a map of the floor
map = fill_map(input)
#Generate a map with 0 values we can later add our risk values into, for part two also creating an index of low spots
(map_risk, basins) = gen_risk_values(map)

print('Sum of risk map is:', map_risk.sum())

print('Solution two:',find_basins(map, basins))