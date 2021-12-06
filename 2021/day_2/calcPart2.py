import re
import os

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/input.txt'
#Our input file to work with
input = open(inputFile, 'r')

#We start at a dept and horizontal value of 0
depth = 0
horizontal = 0

#We've got a new value aim also starting at 0
aim = 0

#Our regular expression to group the direction and number.
exp = '(\w*)[ ](\d)'

#Walk through the inputs one line at a time
for line in input:
    x = re.search(exp, line)
    direction = x.group(1)
    amount = int(x.group(2))
    match direction:
        case 'forward':
            horizontal += amount
            depth += amount*aim #Forward momentum now also impacts depths depending on the value of aim.
        case 'down':
            aim += amount #Aim is a new variable that we now use in up and down instead of depth
        case 'up':
            aim -= amount 

#Print our resulting positions and multiply
print('Depth: '+ str(depth)+', horizontal: '+ str(horizontal))
print('Depth multiplied by horizontal position: '+ str(depth*horizontal))

input.close()