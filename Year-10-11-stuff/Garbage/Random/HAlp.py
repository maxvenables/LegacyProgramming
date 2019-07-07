def gen_board():
    board = []
    for i in range(7):
        board.append([])
        for j in range(7):
            num = (j + 1) + 7 * i
            preItem = str(num)
            if num < 10:
                preItem  = " " + preItem
            preItem = "   " + preItem + "   "
            board[i].append(preItem)
    board.reverse()
    count = 0
    for i in board:
        if count % 2 != 0:
            i.reverse()
        count += 1
    for i in range(15):
        if i % 2 == 0:
            board.insert(i, [])
    for i in range(31):
        if i % 2 == 0:
            board.insert(i, [])
            
    for i in range(len(board)):
        if (i % 4) - 1== 0:
            for j in range(57):
                board[i].append("-")
    
    for i in board:
        for j in range(len(i)):
            if j % 9 == 0:
                i.append("")
        
    
    return board

def print_board(board):
    for i in board:
        for j in i:
            print(j, end="")
        print("")
        
board = gen_board()
print_board(board)