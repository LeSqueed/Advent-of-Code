import re
import collections

filename = 'input.txt'
file = open(filename, 'r')
steps = 40

#Get our input line that we need to work with first.
input = file.readline()
file.readline() #Just passing new line after our input so we don't have to keep this in mind later.
#Read rest of the file.
instructions = [line.rstrip() for line in file]

def list_to_dict(list):
    #Make a dictrionary with our values and replacements.
    new_dict = {}
    for match in list:
        match=match.split('->')
        #Create a dictrionary for each item removing whitespace, instead of storing the value that gets inserted we can store the new value that replaces the original one.
        key = match[0].strip()
        value = match[1].strip()
        #Text to replace it with, insert a # to avoid future matching, remove all #'s at the end of each step.
        replacement = key[0]+'#'+value+'#'+key[1]
        new_dict[match[0].strip()] = replacement
    return new_dict

def replace_match(input_string, match, loops):
    output = input_string
    for i in range(loops):
        for m, r in match.items():
            search = re.search(m,output)
            #Keep going till there is no new match
            while search != None:
                output = re.sub(m, r, output)
                search = re.search(m,output)
        #Remove the # for next iteration
        output = re.sub('#', '', output)
        #print(len(output), output)
    return output

instructions = list_to_dict(instructions)

output = replace_match(input.strip(), instructions, steps)
print(len(output))
count_chars = collections.Counter(output).most_common()

print(count_chars[0])
print(count_chars[-1])
print('Solve 1:', count_chars[0][1]-count_chars[-1][1])

#print(input)
#print(instructions)