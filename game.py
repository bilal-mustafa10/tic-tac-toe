# Tic-tac-toe Game
import random
global playerOneTurn,playerTwoTurn,playerOneWin,playerTwoWin,board,playerOneValues,playerTwoValues,values,ticTacToe
board = [' ' for x in range(10)]
playerOneValues = []
playerTwoValues = []
values = [1,2,3,4,5,6,7,8,9]
playerOneTurn = False
playerTwoTurn = False
playerOneWin = 0
playerTwoWin = 0
ticTacToe = True



def introduction():
    global playerOneName,playerTwoName
    playerOneName = input("Please enter Player 1 Name: ")
    playerTwoName = input("Please enter Player 2 Name: ")
    playerOneName = playerOneName.upper()
    playerTwoName = playerTwoName.upper()


def printBoard(board):
    print('\n')
    print("          " +board[1],end = "  |")
    print("  " +board[2],end = "   | ")
    print(" " +board[3])
    print("          " + "--------------")
    print("          " +board[4],end = "  |")
    print("  " +board[5],end = "   | ")
    print(" " +board[6])
    print("          " + "--------------")
    print("          " +board[7],end = "  |")
    print("  " +board[8],end = "   | ")
    print(" " +board[9])
    



def menu():
    print("=================================================")
    print(playerOneName,"WON: ",playerOneWin,end = "                     ")
    print(playerTwoName,"WON: ",playerTwoWin)
    print()
    if playerOneTurn == True:
        print(playerOneName,"'s TURN")
    elif playerTwoTurn == True:
        print(playerTwoName,"'s TURN")


def startGame():
    global playerOneTurn,playerTwoTurn
    turn = random.randint(1,2)
    if turn == 1:
        playerOneTurn = True
    elif turn == 2:
        playerTwoTurn = True
        
def game():
    global playerOneTurn,playerTwoTurn
    print("")
    print("")
    userInput = int(input("Please enter a Number(1-9) : "))
    
    while (userInput < 1 or userInput > 9) or not(userInput in values):
        print("Incorrect number")
        print("Please try again!")
        userInput = int(input("Please enter a Number(1-9): "))

    
    if playerOneTurn == True:
        playerOneValues.append(userInput)
        values.remove(userInput)       
        board[userInput] = "X"
        playerOneTurn = False
        playerTwoTurn = True
    elif playerTwoTurn == True:
        playerTwoValues.append(userInput)
        values.remove(userInput)
        board[userInput] = "O"
        playerTwoTurn = False
        playerOneTurn = True
 
        
def continueGame():
    global playerOneWin,playerTwoWin,board,playerOneValues,playerTwoValues,values,ticTacToe
    print()
    playAgain = input("Do you want to play again? [Y/N]: ")
    if playAgain == "N" or playAgain == "n" :
        print("\n")
        print("RESULT: ")
        print(playerOneName,"WON: ",playerOneWin)
        print(playerTwoName,"WON: ",playerTwoWin)
        ticTacToe = False
    elif playAgain == "Y" or playAgain == "y":
        board = ['   ' for x in range(10)]
        playerOneValues = []
        playerTwoValues = []
        values = [1,2,3,4,5,6,7,8,9]
        playerOneTurn = False
        playerTwoTurn = False
    
    
def main():
    global playerOneWin,playerTwoWin,board,playerOneValues,playerTwoValues,values,ticTacToe
    introduction()
    print()
    startGame()
    print()
    while ticTacToe == True:
        menu()
        printBoard(board)
        game()

        if (1 in playerOneValues) and (2 in playerOneValues) and (3 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (4 in playerOneValues) and (5 in playerOneValues) and (6 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (7 in playerOneValues) and (8 in playerOneValues) and (9 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (1 in playerOneValues) and (4 in playerOneValues) and (7 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (2 in playerOneValues) and (5 in playerOneValues) and (8 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (3 in playerOneValues) and (6 in playerOneValues) and (9 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (1 in playerOneValues) and (5 in playerOneValues) and (9 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif (3 in playerOneValues) and (5 in playerOneValues) and (7 in playerOneValues):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()


        if (1 in playerTwoValues) and (2 in playerTwoValues) and (3 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (4 in playerTwoValues) and (5 in playerTwoValues) and (6 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (7 in playerTwoValues) and (8 in playerTwoValues) and (9 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (1 in playerTwoValues) and (4 in playerTwoValues) and (7 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (2 in playerTwoValues) and (5 in playerTwoValues) and (8 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (3 in playerTwoValues) and (6 in playerTwoValues) and (9 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (1 in playerTwoValues) and (5 in playerTwoValues) and (9 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()
        elif (3 in playerTwoValues) and (5 in playerTwoValues) and (7 in playerTwoValues):
            print(playerTwoName,"WON! ")
            playerTwoWin += 1
            continueGame()

               
    
if __name__ == "__main__":
    main()

            
        
        
        
    

