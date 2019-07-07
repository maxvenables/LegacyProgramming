class player(): #Create a player class for easy code reuse
    def __init__(self): 
        self.coords = [0 , 0] #Sets players starting coords as (0, 0)
        self.icon = "p" #Sets up icon ready for a 1 or 2 to be added to the end
    def change_coords(self, newX, newY): #creates a function that will be used to acsess players coords
        self.coords[0] = newX 
        self.coords[1] = newY
        
class obstacle():
    def __init__(self, coords, warpCoords, typ):
        self.coords = coords
        self.warpCoords = warpCoords
        
        
def make_board(typ = "none"): #will generate multi dimensional array full of " " characters  , takes a tpye, either num, for a numbered board or none for a blank one, none is set as defult value
    board = [] #store master array in variable board
    for i in range(7):
        board.append([]) #Adds inner arrays to board
        for j in range(7):
            if typ == "num": #checks if the program is creating a numbered grid
                num = str((j + 1) + (7 * i)) #Gets value for cell
                if len(str(num)) <= 1: #checks whether or not num is single digit
                    num = " " + num #adds extra space to num to accomodate for ^
                board[i].append(str(num)) #Adds new values to inner arrays
            else:
                board[i].append("  ") #Adds elements to inner arrays
    board.reverse() #Reverses board elements, causes bottom to start at "1" instead of "43"
    for (i, v) in enumerate(board): #for loop will traverse board
        if (i % 2) - 1 == 0:
            v.reverse() # makes board wind like specification
    return board

def print_board(pBoard, oBoard, nBoard): #Function will print board, takes values of player coords and obstacle coords
    counter1 = 0 #sets a counter for oBoard's first index
    counter2 = 0 #sets a counter for nBoard's first index
    counter3 = 0 #sets a counter for pBoard's first index
    for i in range(29):
        if i % 4 == 0: # Checks if border between lines should be added
            for j in range(54):
                print("-", end="") #Adds border
            print()
        elif (i % 4) - 1 == 0: #Checks if obstacle should be added
            for k in range(7):
                print("  |  " + oBoard[counter1][k], end="") #Adds obstacles
            print("  |  ")
            counter1 += 1 #Iterates counter
        elif (i % 4) - 2 == 0: #Checks if player should be added
            for k in range(7):
                print("  |  " + nBoard[counter2][k], end="") #Adds players
            counter2 += 1 #Iterates counter
            print("  |  ")
        elif (i % 4) - 3 == 0: #Checks if player should be added
            for k in range(7):
                print("  |  " + pBoard[counter3][k], end="") #Adds players
            counter3 += 1 #Iterates counter
            print("  |  ")
        
            
playerBoard = make_board()
obstacleBoard = make_board()
numberBoard = make_board("num")
playerBoard[5][4] = "p1"
obstacleBoard[1][2] = "l1"
obstacleBoard[4][2] = "l1"
print_board(playerBoard, obstacleBoard, numberBoard)
