from statistics import mean
from math import ceil, floor

filename = 'input.txt'
input = [int(x) for x in open(filename, 'r').readline().split(',')] #convert input into an array of integers


def solve_1(input):
    least_fuel = sum(input) #Set max fuel to all numbers combined so that the initial run is always lower than this.
    for sub in input:
        #We start at 0 fuel consumed.
        fuel_consumed = 0
        for position in input:
            fuel_consumed += abs(sub-position)
        #Update least consumed fuel as long as it is not comparing against itself.
        least_fuel = fuel_consumed if fuel_consumed < least_fuel else least_fuel
    return least_fuel

def solve_2(input, round):
    #Get the right value from the mean but have to either round up or down. No clue how to check which one is the right way to go so let's just do both.
    if round == 'floor':
        input_mean = floor(mean(input))
    else:
        input_mean = ceil(mean(input))
    for _ in input:
        #We start at 0 fuel consumed.
        fuel_consumed = 0
        for position in input:
            steps = abs(position - input_mean)
            fuel_consumed += steps*(steps+1)/2 #sum of n terms
        #Update least consumed fuel as long as it is not comparing against itself.
    return int(fuel_consumed)

print('Solution 1:', solve_1(input))
print('Solution 2:', solve_2(input, 'ceil'), 'or', solve_2(input, 'floor'))