filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 

#Find syntax errors, for part one only find cases with corrupt lines not incomplete for part 1.

#Possible symbols: (, [, { and < (total of 4)
#Store history of last opened tag. The next closing tag should match the last open tag.
syntax_history = []

#id's for possible symbols:
symbol_ids = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2, '<': 3, '>': 3}
#Set of opening or closing symbols
symbols_open = set('( [ { <')
symbols_close = set(') ] } >')

def solve_1(input):
    #) = 3, ] = 57, } 1197 and > 25137 points per occurence.
    score_values = [3, 57, 1197, 25137]
    found_errors = [0]*4
    score = 0

    for line in input:
        syntax_check = [0]*4
        
        for char in line:
            #Check only opening tags.
            if(char in symbols_open):
                syntax_history.append(symbol_ids[char])
            elif(char in symbols_close):
                if symbol_ids[char] != syntax_history[-1]:
                    found_errors[symbol_ids[char]] += 1
                    break
                else:
                    syntax_history.pop(-1)
    for index, found  in enumerate(found_errors):
        score += found*score_values[index]
    return score

print(solve_1(input))
