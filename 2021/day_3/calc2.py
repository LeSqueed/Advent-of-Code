import os
import re

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/sampleInput.txt'

input = open(inputFile, 'r')
length = 2 
count = []
count = [0 for i in range(length)]
total = 0 #Total amount of lines.

offset = 0 #Offset we will be using to get next bit as we loop through.
#We want to run through the lines getting the most common first, second etc. value from new sets as we go.
oxygen = []

while length > 1:
    #bit value to look for.
    value = input.readline()[offset] #We now have the value we want to look for in our data
    for line in input:
        length = len(line)
         #Strip the new line character.
        line = line.strip('\n') 
        if line[offset] == value:
            oxygen.append(line)
    length = length-len(oxygen)
    offset =+ 1
print(oxygen)
        

