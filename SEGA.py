count = [0,0,0,1,1,1,0,0,0]

def isWin(b):
    # horizontal lines
    for i in [0, 3, 6]:
        if (b[i] == b[i + 1]) and (b[i] == b[i + 2]) and  CheckMove(b[i]):
            return b[i]
            # vertical lines
    for i in [0, 1, 2]:
        if (b[i] == b[i + 3]) and (b[i] == b[i + 6]) and CheckMove(b[i]):
            return b[i]
            # diagonal lines
    if (b[0] == b[4]) and (b[0] == b[8]) and  CheckMove(b[0]):
        return b[0]
    elif (b[2] == b[4]) and (b[2] == b[6]) and (CheckMove(b[2])):
        return b[2]
    else:
        return 0

# CheckMove
# check if the char is X or O not space and check if the X/O is moved once or not
def CheckMove(ch):
    if (ch == -1 or ch == 'X')and checkCountX():
        return True
    elif (ch == 1 or ch =='O') and checkCountO():
        return True
    return False

# checkCountX
# check if Player 1 (X) is moved or not
def checkCountX():
    global count
    for i in range(0,3):
        if count[i]==0:
            return False
    return True

# checkCountO
# check if Computer (O) is moved or not
def checkCountO():
    for i in range(6,9):
        if count[i]==0:
            return False
    return True

def countWins (b , player):
    old = []
    counter = 0
    for i in range(0, 9):
        if b[i] == 0:
            old.append(i)
            b[i] = player
    for i in [0, 3, 6]:
        if (b[i] == b[i + 1]) and (b[i] == b[i + 2]) and (b[i] == player):
            counter += 1
    for i in [0, 1, 2]:
        if (b[i] == b[i + 3]) and (b[i] == b[i + 6]) and (b[i] == player):
            counter += 1
    if (b[0] == b[4]) and (b[0] == b[8]) and (b[0] == player):
        counter += 1
    elif (b[2] == b[4]) and (b[2] == b[6]) and (b[2] == player):
        counter += 1
    for i in old:
        b[i] = 0
    return counter

# heu_Value
# To make a heuristic value for given board by counting the chances of O-X to Win
def heu_value(b) :
    countO = countWins(b,1)
    countX = countWins(b,-1)
    return countO-countX

def minimax(board,player,currDepth,scored):
    winner = isWin(board)
    if (winner != 0):
        return winner * 4
    if (currDepth == 4): return heu_value(board)
    global count
    score = scored
    currDepth += 1
    for played in findState(board, player):
        for empty in findState(board, 0):
            board[empty] = player
            board[played] = 0
            state = count[played]
            count[played] = 1
            thisScore = minimax(board,player*-1, currDepth,scored*-1)
            if player == -1:
                if (thisScore < score):
                    score = thisScore
            elif player == 1:
                if (thisScore > score):
                    score = thisScore
            board[empty] = 0
            board[played] = player
            count[played] = state
    return score

# findState
# find the char in given board and return list
def findState(board,ch):
    index = []
    for i in range(0,9):
        if board[i]==ch :
            index.append(i)
    return index

# ComputerMove
# return The best Move and Replace
def computerMove(board):
    board = convertInt(board)
    global count
    score = -5 # Losing moves are preferred to no move
    for played in findState(board,1):
        for empty in findState(board, 0):
            currDepth = 0
            board[empty] = 1
            board[played] = 0
            state = count[played] # state to save if the pos is moved or not
            count[played] = 1
            tempScore = minimax(board,-1, currDepth,5)
            #print tempScore
            if tempScore > score or tempScore == score and ((state == 0 and score !=4) or isWin(board)):
                score = tempScore
                move = empty
                replace = played
            board[empty] = 0
            board[played] = 1
            count[played] = state
    return (move,replace)

def convertInt(board):
    b = list(board) # to not change in the Main board
    for i in range(0,9):
        b[i] = gridChar(b[i])
    return b

# gridChar
# convert from char to integer number
def gridChar(ch) :
    if ch == 'X':
         return -1
    elif ch == ' ':
        return 0
    elif ch == 'O':
        return 1

def draw(board):
        print (" _______________________\n" +
               "|       |       |       |\n" + "|   " + board[0] + "   |   " + board[1] + "   |   " + board[2] + "   |\n" +
               "|_______|_______|_______|\n" + "|       |       |       |\n" + "|   " + board[3] + "   |   " + board[
                   4] + "   |   " + board[5] + "   |\n" +
               "|_______|_______|_______|\n" + "|       |       |       |\n" + "|   " + board[6] + "   |   " + board[
                   7] + "   |   " + board[8] + "   |\n" +
               "|_______|_______|_______|\n")

# validMoves
# Returns the list of valid moves for a given board
def validMoves(board):
    valid = []
    for pos in range(0, 9):
        if board[pos] == ' ':
            valid.append(pos)
    return valid

# playerMove
# Attempts to make a move X on the board
# Returns (True) if a valid move and valid Replace , with newBoard being a new game board
# Returns (False) if an invalid move, with the board being unchanged
def playerMove(board, move,replace):
    if move in validMoves(board) and not(replace in validMoves(board)) and (board[replace] == 'X'):
        board[replace] = ' '
        board[move] = 'X'
        return True
    else:
        return False

def play(board):
    global count
    draw(board)
    if (isWin(board) != 0):
        print (" ******** The Winner is  " + (isWin(board)) + " *********")
    else:
        print "Valid Places :", validMoves(board)
        replace = raw_input("Your Choice : ")
        move = raw_input("Place in OR type exit to exit the Game : ")
        if (move == "exit"):
            exit()
        else:
            if (replace != "" and move != ""):
                replace = int(replace)
                move = int(move)
                valid = (playerMove(board, move,replace))
                if (valid):
                    count[replace] = 1
                    print "\n  ******** Ok ********\n"
                    if (0 != isWin(board)):
                        print (" ******** The Winner is  " + isWin(board) + " *********")
                        draw(board)
                    else:
                        (move,replace)=computerMove(board)
                        board[replace] = ' '
                        count[replace] = 1
                        board[move] = 'O'
                        play(board)
                else:
                    print ("\n** Invalid Place! **\n")
                    play(board)
            else:
                print ("\n ** Please,Enter a valid Place ** \n")
                play(board)

if __name__ == '__main__':
    print ("\t\t\t\t*** Welcome in Sega Game ^_^ ***\n")
    start = raw_input("To Start the Game press Enter OR any key to exit")
    if (start == ""):
        play(['X', 'X', 'X', ' ', ' ', ' ', 'O', 'O', 'O'])
    else:
        exit()
