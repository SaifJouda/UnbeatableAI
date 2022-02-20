import random

boards=[]
for i in range(9):
    boards.append(' ')

def printBoard(board):
    print('['+board[0]+']['+board[1]+']['+board[2]+']')
    print('['+board[3]+']['+board[4]+']['+board[5]+']')
    print('['+board[6]+']['+board[7]+']['+board[8]+']')

def numEmptyLeft(board):
    x=0
    for i in range(9):
        if(board[i]==' '):
            x+=1
    return x

def checkOne(x,y,z,symbol,board):
    num=0
    if (board[x]==symbol and board[y]==' ' and board[z]==' '):
        num=1
    if (board[x]==' ' and board[y]==symbol and board[z]==' '):
        num=1
    if (board[x]==' ' and board[y]==' ' and board[z]==symbol):
        num=1
    return num

def numOne(symbol,board):
    x=0
    x+=checkOne(0,1,2,symbol,board)
    x+=checkOne(3,4,5,symbol,board)
    x+=checkOne(6,7,8,symbol,board)
    x+=checkOne(0,3,6,symbol,board)
    x+=checkOne(1,4,7,symbol,board)
    x+=checkOne(2,5,8,symbol,board)
    x+=checkOne(0,4,8,symbol,board)
    x+=checkOne(2,4,6,symbol,board)
    return x
    
def checkTwo(x,y,z,symbol,board):
    num=0
    if (board[x]==symbol and board[y]==symbol and board[z]==' '):
        num=1
    if (board[x]==' ' and board[y]==symbol and board[z]==symbol):
        num=1
    if (board[x]==symbol and board[y]==' ' and board[z]==symbol):
        num=1
    return num

def numTwo(symbol,board):
    x=0
    x+=checkTwo(0,1,2,symbol,board)
    x+=checkTwo(3,4,5,symbol,board)
    x+=checkTwo(6,7,8,symbol,board)
    x+=checkTwo(0,3,6,symbol,board)
    x+=checkTwo(1,4,7,symbol,board)
    x+=checkTwo(2,5,8,symbol,board)
    x+=checkTwo(0,4,8,symbol,board)
    x+=checkTwo(2,4,6,symbol,board)
    return x
    


    

def checkWin(symbol,board):
    if (board[0]==symbol and board[1]==symbol and board[2]==symbol):
        return True
    if (board[3]==symbol and board[4]==symbol and board[5]==symbol):
        return True
    if (board[6]==symbol and board[7]==symbol and board[8]==symbol):
        return True
    if (board[0]==symbol and board[3]==symbol and board[6]==symbol):
        return True
    if (board[1]==symbol and board[4]==symbol and board[7]==symbol):
        return True
    if (board[2]==symbol and board[5]==symbol and board[8]==symbol):
        return True
    if (board[0]==symbol and board[4]==symbol and board[8]==symbol):
        return True
    if (board[2]==symbol and board[4]==symbol and board[6]==symbol):
        return True

def eval(board):
    if checkWin('X',board):
        return 100
    else:
        x=3*numTwo('X',board)+numOne('X',board)-4*numTwo('O',board)-numOne('O',board)
        return x




def AImove(board):
    bestScore = -100
    bestMove = 0
    for i in range(9):
        if board[i]==' ':
            board[i]='X'
            evalScore=eval(board)
            print("for: ",i+1," score: ",evalScore)
            if evalScore > bestScore:
                bestScore=evalScore
                bestMove=i
            board[i]=' '
    print('best move is: ',bestMove+1)
    return bestMove

def insert(board):
    inserted=False
    while inserted ==False:
        y = input()
        x = int(y)-1
        if (x>=0 and x<9 and boards[x]==' ' ):
            boards[x]='O'
            inserted=True
        else:
            print("Incorrect, try again")

def main():
    gameOver = False
    ran=random.randint(0, 8)
    print("Select Difficulty:")
    print("Hard (you can win only on this difficulty): (type 'h')")
    print("Undefeatable: (type anything else)")


    start=input()
    if(start!='h'):
        boards[0]='X'

    

    while gameOver == False:
        print('[1][2][3]')
        print('[4][5][6]')
        print('[7][8][9]\n')
        printBoard(boards)
        print("Input (1-9):")
        insert(boards)

        if (checkWin('O',boards)==True):
            print("Congratualtions, you WIN!")
            gameOver=True
        else:    
            aiMove=AImove(boards)
            boards[aiMove]='X'

            if (checkWin('X',boards)==True):
                printBoard(boards)
                print("You Lose, The AI is undefeatable")
                gameOver=True

            if numEmptyLeft(boards)==0: 
                printBoard(boards)
                print("Draw, you will never win")
                gameOver=True

        
        
            



if __name__ == '__main__':
    main()
