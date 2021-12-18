import numpy as np

filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 

instructions =[]
dots = []

#Dimensions of our array, we will get the max out of our input.
R = 0
C = 0

#Split our input into the values that indicate dot locations and the fold instructions.
for line in input:
    if "x" in line:
        instructions.append(["x", int(''.join(filter(str.isdigit, line)))])
    elif "y" in line:
        instructions.append(["y", int(''.join(filter(str.isdigit, line)))])
    elif len(line) > 0:
        dots.append(tuple([int(x) for x in line.strip().split(',')]))

for x, y in dots:
    if x > R:
        R = x
    if y > C:
        C = y

R = R+1
C = C+2

#Set type to boolean so we can use bitwise operators. 
man_page = np.zeros((R, C), dtype=bool)

#Fill in the dots, 1 will represent a dot.
for i in dots:
    man_page[i] = 1

def solve(instructions, page, code = False):
    #Now we need to "fold" based on x or y.
    for fold in instructions:
        print(fold)
        fold[1] = int(fold[1])
        if fold[0] == 'x':
            page = np.delete(page,int(fold[1]), axis = 0)
            half_1, half_2 = np.vsplit(page,2)
            half_2 = np.flipud(half_2)
            page = half_2 | half_1
        else:
            page = np.delete(page, int(fold[1]), axis = 1)
            half_1, half_2 = np.hsplit(page,2)
            half_2 = np.fliplr(half_2)
            page = half_1 | half_2
        if code == False:
            return int(page.sum())
    #Change type and formatting to make it easier to read.
    page = page.astype(str)
    page = np.where(page == 'False', '.', page)
    page = np.where(page == 'True', '#', page)
    code = page.tolist()
    #Reverse the code so we can scroll from buttom upwards to read it
    code.reverse()
    for letter in code:
        print(''.join(letter))
    #print(page.astype(int))

print('Solve 1:', solve(instructions, man_page, False))
solve(instructions, man_page, True)