def mark_boards(num, boards):
    R = len(boards[0]) #Count the row length
    C = len(boards[0][0]) #Count the columns
 
    for board in boards:
        for r in range(R):
            for c in range(C): #For item
                if board[r][c] == num:
                    board[r][c] = -1
 
def find_winner(boards, winners):
    R = len(boards[0]) 
    C = len(boards[0][0]) 
    winner = None
 
    ##Iterate through board, assigning te id of the board to i
    for i, board in enumerate(boards): 
        if i in winners:
            continue
 
        for r in range(R):
            curr = 0
            for c in range(C):
                if board[r][c] == -1:
                    curr += 1

            #If current amount of marks equals length of column it's a win
            if curr == C:
                winners.add(i)
                winner = board
 
        for c in range(C):
            curr = 0
            for r in range(R):
                if board[r][c] == -1:
                    curr += 1
 
            if curr == R:
                winners.add(i)
                winner = board
 
    return winner
 
def get_unmarked_nums(board):
    unmarked_nums = []
    R = len(board)
    C = len(board[0])
 
    for r in range(R):
        for c in range(C):
            if board[r][c] != -1: #If value is unmarked add it to the list
                unmarked_nums.append(board[r][c])
 
    return unmarked_nums
 
def solve_1(nums, boards):
    winners = set() #Create an empty set to later fill
 
    for num in nums:
        mark_boards(num, boards) #Checks if number is present on this board set's the value to -1 if it is to mark it. (0 being lowest number on boards)
        winner = find_winner(boards, winners) #Let's find out what board wins
 
        if winner:
            return sum(get_unmarked_nums(winner)) * num
 
    return -1
 
def solve_2(nums, boards):
    
    winners = set()
 
    for num in nums:
        mark_boards(num, boards)
        winner = find_winner(boards, winners)
 
        #Check if we got all the possible winners.
        if len(winners) == len(boards):
            return sum(get_unmarked_nums(winner)) * num
 
    return -1 
 
with open('input.txt') as f:
    nums = [int(x) for x in f.readline().strip().split(',')] #Random numbers given to us in the file.
    boards = [] 

    f.readline() #Reading the first line with the random numbers

    for board in f.read().split('\n\n'): ##Splitting on double line to get the individual boards and iterating through them.
        tmp = []

        for row in board.split('\n'): #Get each row of the board as a seperate list item.
            tmp.append([int(num) for num in row.split()]) #Split each row item into seperate integers

        boards.append(tmp) #add each board as a seperate list item

    #Copy board use it for each part of the puzzle
    #Should not work? No deep copy.
    boards1 = boards
    boards2 = boards
    print(solve_1(nums, boards1))
    print(solve_2(nums, boards2))