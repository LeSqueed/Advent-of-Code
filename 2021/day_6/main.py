filename = 'input.txt'
input = [int(x) for x in open(filename, 'r').readline().split(',')] #convert input into a list of integers
days = 254 #Amount of days to iterate through.
types = 8 #Types of fishes based on their age.

#Slow way that breaks down at longer ranges. Increases the size of the list and iterates through the new list each time. Eventually list gets to a size that it takes too long to process.
def count_fish_part1(input, days):
    for _ in range(days):
        for i in range(len(input)):
            if input[i] == 0:
                input.append(8)
                input[i] = 7
            input[i] -= 1
    return len(input)

def count_fish(input,days):
    fishes = []
    for n in range(types+1): #The possible number of each fish
        fishes.append(0)
    for n in input:
        fishes[n] += 1 #Populate our list of fishes by age with the initial values.
    
    new_fishes = 0
    #Iterate through the days.
    for _ in range(days):
        new_fishes = fishes[0]*1 #Everytime there's a fish with value at 0 add one new fish.
        for fish in range(len(fishes)):
            if fish == 0: #If lowest value we need to add a fish to the row of fishes with value 8.
                fishes[7] += fishes[fish]
            else: #Else we need to move the fish over to the row one value lower than it is in now.
                fishes[fish-1] += fishes[fish]
            fishes[fish] -= fishes[fish]
        fishes[8] += new_fishes #Add the new fishes into the table for the next round of calculations.
    return fishes
    #We now know the initual values of how many of each type of fish we have.

#Sum to count all the numbbers in the list returned.
print(sum(count_fish(input, days)))