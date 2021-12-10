from statistics import median
filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 

#Find syntax errors, for part one only find cases with corrupt lines not incomplete for part 1.

#Possible symbols: (, [, { and < (total of 4)

#id's for possible symbols:
symbol_ids = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2, '<': 3, '>': 3}
#Set of opening or closing symbols
symbols_open = set('( [ { <')
symbols_close = set(') ] } >')

#For solve 2 let's store the lines found with errors so we can easily remove them from the input later.
lines_with_errors = []

def solve_1(input):
    #) = 3, ] = 57, } 1197 and > 25137 points per occurence.
    #Store history of last opened tag. The next closing tag should match the last open tag.
    syntax_history = []
    score_values = [3, 57, 1197, 25137]
    found_errors = [0]*4
    score = 0

    for index, line in enumerate(input):        
        for char in line:
            #Check only opening tags.
            if(char in symbols_open):
                #Add ID for tag to our history
                syntax_history.append(symbol_ids[char])
            #If not an opening tag check if closing tag.
            elif(char in symbols_close):
                #Check if this character type matches with the last value in our index.
                if symbol_ids[char] != syntax_history[-1]:
                    #If it doesn't match we add one of this type to our error counter
                    found_errors[symbol_ids[char]] += 1
                    #For solve 2 we need to discard the lines from solve one, doing that here.
                    lines_with_errors.append(index)
                    break
                else:
                    #Remove from our histroy if we found a matching closing tag.
                    syntax_history.pop(-1)
    for index, found  in enumerate(found_errors):
        #Calculate our end score
        score += found*score_values[index]
    return score

def solve_2(input):
    #Remove lines from solve 1 from our dataset, sort in reverse first so we remove the last low first and move our way backwards.
    lines_with_errors.sort(reverse=True)
    for i in lines_with_errors:
        input.pop(i)
    #Part two requires us to replace incorrect end tags with the correct one. We should be able to keep using our index and history for this

    corrected_errors = [0]*4
    score = []
    for index, line in enumerate(input):      
        syntax_history = []
        for char in line:
            #Check only opening tags.
            if(char in symbols_open):
                #Add ID for tag to our history
                syntax_history.append(symbol_ids[char])
            #If not an opening tag check if closing tag.
            elif(char in symbols_close):
                #Remove from history.
                syntax_history.pop(-1)

        #We now have values remaining in our history, these are the values that still need to be closed from end to start, so let's reverse it first to make it easier to work with.
        syntax_history.reverse()

        #Now we need to do our maths. Start with a score of 0 -> multiply score by 5 -> Add point value of character.
        #Score values characters: ) = 1, ] = 2, } = 3 and > = 4.
        
        n_score = 0
        for char in syntax_history:
            score_values = [1, 2, 3, 4]
            n_score = n_score*5 + score_values[char]
            #syntax_history.pop(0)
        score.append(n_score)
    #We've now got to sort the scores and return the median one, for this one we need to check if we've got an even or uneven length.
    score.sort()
    if len(score) % 2 == 1:
        return score[len(score)//2]
    else:
        return score[(len(score)/2)-1]+score[(len(score)/2)+1]//2

        
print('Solution 1:',solve_1(input))

print('Solution 2:', solve_2(input))