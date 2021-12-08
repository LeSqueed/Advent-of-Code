filename = 'input.txt'
input = [line.rstrip() for line in open(filename)] 

values = [0]*10
outputs = []

def find_number(digit):
    #Return the easy numbers with unique lengths.
    match len(digit):
        case 2:
            values[1] = ''.join(sorted(digit))
            return 1
        case 3:
            values[7] = ''.join(sorted(digit))
            return 7
        case 4:
            values[4] = ''.join(sorted(digit))
            return 4
        case 7:
            values[8] = ''.join(sorted(digit))
            return 8
    return False

def solve_1(input):
    occurences = 0
    for data in input:
        #Split input on |, only use the values after the | and clean up whitespace in front
        data = ''.join(data.split('|')).lstrip().rstrip().split(' ')
        #Now we have every digit after the | as a seperate item
        for digit in data:
            #To retrieve the number, pass it onto a new function
            number = find_number(digit)
            if number:
                occurences += 1
    print('Amount of simple numbers:', occurences)

def index(data):
    #Split input on |, taking data from the front to build an index for numbers
    data = data.split('|')[0].rstrip().split(' ')
    digits_list = []
    for digit in data:
        digits_list.append(digit)
    
    #Sort list by length
    digits_list = sorted(digits_list, key=len)
    #We can't just pass through the data cause we need information from certain numbers first to find out what the others are.
    find_number(digits_list[0])
    find_number(digits_list[1])
    find_number(digits_list[2])
    find_number(digits_list[9])
    
    #Reverse our list so we get the numbers with length of 6 first, we need these to find out what the numbers with length of 5 are.
    digits_list.reverse()
    for digit in digits_list:
        digit = ''.join(sorted(digit))
        if len(digit) == 6:
            if set(str(values[4])).issubset(digit):
                values[9] = digit
            elif set(str(values[1])).issubset(digit):
                values[0] = digit
            else:
                values[6] = digit
        elif len(digit) == 5:
            if set(str(values[1])).issubset(digit):
                values[3] = digit
            elif set(digit).issubset(str(values[6])):
                values[5] = digit
            else:
                values[2] = digit


    

def solve_2(input):
    for data in input:
        result = ''
        index(data)
        #Split input on |, only use the values after the | and clean up whitespace in front
        data = data.split('|')[1].lstrip().split(' ')
        #Now we have every digit after the | as a seperate item
        result = '' #store total of all numbers in here
        for digit in data:
            digit = ''.join(sorted(digit))
            #convert to string so we can add each number at the end.
            result += str(values.index(digit))
        #Go back to int when storing it in our list for the sum.
        outputs.append(int(result))
    return sum(outputs)


solve_1(input)
print(solve_2(input))