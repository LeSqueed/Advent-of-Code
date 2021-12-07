import os

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/input.txt'

input = open(inputFile, 'r')
higher = 0
firstLine = ''
prevLine = ''
arr = []

#Build an array with the values we need.
for line in input:
    if firstLine == '':
        print('Populating values')
    elif sum == '':
        arr.append(int(firstLine)+int(prevLine)+int(line))
    else:
        arr.append(int(firstLine)+int(prevLine)+int(line))
    firstLine = prevLine
    prevLine = line


input.close() #Have no need for the file anymore, let's close it.

#Now we got a new array with the values to compare.
prevValue = ''
for value in arr:
    if prevValue != '':
        if int(value) > int(prevValue):
            higher += 1
    prevValue = value

print("Value was higher "+str(higher)+" times.")