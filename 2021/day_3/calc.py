import os
import re

dir = dir_path = os.path.dirname(os.path.realpath(__file__))
inputFile = dir+'/input.txt'

input = open(inputFile, 'r')
length = len(input.readline().strip('\n')) #Get the length of our inputs
count = []
count = [0 for i in range(length)]
total = 0 #Total amount of lines.

for line in input:
    run = 0
    line = line.strip('\n') #remove new line character
    result = list(map(int, line))
    for i in result:
        if i == 1:
            count[run] += 1
        else:
            count[run] -= 1
        run += 1

gamma = '' #resulting binary value
epsilon = '' 
for i in count:
    if i > 1:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2) #Convert binary to dec.
epsilon = int(epsilon, 2)

print(gamma*epsilon)
    
        
input.close()