import os

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/input.txt'

input = open(inputFile, 'r')
higher = 0
prevLine = ''

for line in input:
    if prevLine == '':
        prevLine = line
    else:
        if int(line) > int(prevLine):
            higher += 1
    prevLine = line

print("Amount of higher values: "+str(higher))
input.close()