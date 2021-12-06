import re
import os

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/input.txt'
#Our input file to work with
input = open(inputFile, 'r')

#We start at a dept and horizontal value of 0
depth = 0
horizontal = 0

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
        case 'down':
            depth += amount
        case 'up':
            depth -= amount 

#Print our resulting positions and multiply
print('Depth: '+ str(depth)+', horizontal: '+ str(horizontal))
print('Depth multiplied by horizontal position: '+ str(depth*horizontal))

input.close()