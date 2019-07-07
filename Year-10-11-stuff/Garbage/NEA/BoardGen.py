def gen_board(): 
    """
    Function that creates board, will return completed board at end of function
    """
    board = [] #Master array stored in variable 'board', will contain all inner arrays
    
    for i in range(7): #for loop to generate inner ararys, range is '8' as there are 7 rows
        board.append([]) #Adds a new array into 'board', each represents a new row in the board
        for j in range(7): #for loop to generate members of inner arrays, effectively creating columns 
            num = str((j + 1) + (7 * i)) #Gets value for cell
            if len(str(num)) <= 1: #checks whether or not num is single digit
                num = " " + num #adds extra space to num to accomodate for ^
            
            board[i].append(str(num)) #Adds new values to inner arrays
    board.reverse() #Reverses board elements, causes bottom to start at "1" instead of "43"
    for (i, v) in enumerate(board): #for loop will traverse board
        if i % 2 == 0:
            v.reverse() # makes board wind like specification
            
            
    return board #board is returned as a variable

def outputBoard(board):
    """
    Function to print the board
    """
    for i in board: #For loop traverses board
        for j in i: #For loop traverses inner arrays
            print(j, end="")
        print("")
            
        



board = gen_board()
outputBoard(board)