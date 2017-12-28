import random

diceX = int()
diceY = int()
betAmount = int()
cashWon = int()
gridChoice = int(0)

def generateDiceX(): # This function is to generate a dice representing x-axis for the player.
    global diceX # I made this variable global so i can use it outside the function.
    pressEnter = input("\tPress 'Enter' to roll a dice for x-axis.. ") # I used this pressEnter all over the code to help the user understand every step of the game.
    diceX = random.randint(1, 6) # This choose a number from 1 to 6 randomly.
    if diceX == 1:
        print("\t _________")
        print("\t|         |")
        print("\t|         |")
        print("\t|    *    |")
        print("\t|         |")
        print("\t|_________|\n")
    elif diceX == 2:
        print("\t _________")
        print("\t|         |")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|         |")
        print("\t|_________|\n")
    elif diceX == 3:
        print("\t _________")
        print("\t|         |")
        print("\t|       * |")
        print("\t|    *    |")
        print("\t| *       |")
        print("\t|_________|\n")
    elif diceX == 4:
        print("\t _________")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|_________|\n")
    elif diceX == 5:
        print("\t _________")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|    *    |")
        print("\t| *     * |")
        print("\t|_________|\n")
    else:
        print("\t _________")
        print("\t|         |")
        print("\t| *  *  * |")
        print("\t|         |")
        print("\t| *  *  * |")
        print("\t|_________|\n")
    print("\tYou got number {} for x-axis!".format(diceX))
    print("\n\t-------------------------------------------\n")

def generateDiceY(): # This function is to generate a dice representing y-axis for the player.
    global diceY # I made this variable global so i can use it outside the function.
    pressEnter = input("\tPress 'Enter' to roll a dice for Y-axis.. ") # I used this pressEnter all over the code to help the user understand every step of the game.
    diceY = random.randint(1, 6) # This choose a number from 1 to 6 randomly.
    if diceY == 1:
        print("\t _________")
        print("\t|         |")
        print("\t|         |")
        print("\t|    *    |")
        print("\t|         |")
        print("\t|_________|\n")
    elif diceY == 2:
        print("\t _________")
        print("\t|         |")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|         |")
        print("\t|_________|\n")
    elif diceY == 3:
        print("\t _________")
        print("\t|         |")
        print("\t|       * |")
        print("\t|    *    |")
        print("\t| *       |")
        print("\t|_________|\n")
    elif diceY == 4:
        print("\t _________")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|_________|\n")
    elif diceY == 5:
        print("\t _________")
        print("\t|         |")
        print("\t| *     * |")
        print("\t|    *    |")
        print("\t| *     * |")
        print("\t|_________|\n")
    else:
        print("\t _________")
        print("\t|         |")
        print("\t| *  *  * |")
        print("\t|         |")
        print("\t| *  *  * |")
        print("\t|_________|\n")
    print("\tYou got number {} for y-axis!".format(diceY))
    print("\n\t-------------------------------------------\n")

def cls(): # This function is to clear the screen.
    print("\n" * 100)    

def printGrid1(): # This function is to show the grid.
    text_file = open("grid1.txt", "r") # Opens grid1.txt in read mode.
    print(text_file.read(),"\n") # The grid is already drawn in the file grid1.txt.
    text_file.close() # Closes the text file that was in read mode.


def grid1GameOutcome(): # This function is to determine whether the user win the game or not, and if they won what multiplier did they get.
    global diceX, diceY,WM #I made this variable global so i can use it outside the function.
    if diceX == 1 and diceY == 2:
        WM=2 # This variable collects the Win Multiplier.
        wonX2()
    elif diceX == 1 and diceY == 3:
        WM=2
        wonX2()
    elif diceX == 1 and diceY == 5:
        WM=2
        wonX2()
    elif diceX == 2 and diceY == 1:
        WM=2
        wonX2()
    elif diceX == 2 and diceY == 4:
        WM=2
        wonX2()
    elif diceX == 2 and diceY == 6:
        WM=2
        wonX2()
    elif diceX == 3 and diceY == 3:
        WM=2
        wonX2()
    elif diceX == 3 and diceY == 6:
        WM=2
        wonX2()
    elif diceX == 4 and diceY == 1:
        WM=2
        wonX2()
    elif diceX == 4 and diceY == 2:
        WM=2
        wonX2()
    elif diceX == 4 and diceY == 5:
        WM=2
        wonX2()
    elif diceX == 5 and diceY == 1:
        WM=2
        wonX2()
    elif diceX == 5 and diceY == 3:
        WM=2
        wonX2()
    elif diceX == 5 and diceY == 5:
        WM=2
        wonX2()
    elif diceX == 6 and diceY == 2:
        WM=2
        wonX2()
    elif diceX == 6 and diceY == 4:
        WM=2
        wonX2()
    elif diceX == 6 and diceY == 6:
        WM=2
        wonX2()
    else:
        WM=0
        lost()

def printGrid2(): # This function is to show the grid.
    text_file = open("grid2.txt", "r") # Opens grid2.txt in read mode.
    print(text_file.read(),"\n") # The grid is already drawn in the file grid2.txt.
    text_file.close() # Closes the text file that was in read mode.

def grid2GameOutcome(): # This function is to determine whether the user win the game or not ,and if he won what multiplier did he get.
    global diceX, diceY,WM # I made this variable global so i can use it outside the function.
    if diceX == 1 and diceY == 1:
        wonX7()
        WM=7 # This variable collects the Win Multiplier.
    elif diceX == 1 and diceY == 3:
        WM=2
        wonX2()
    elif diceX == 1 and diceY == 5:
        WM=2
        wonX2()
    elif diceX == 2 and diceY == 1:
        WM=2
        wonX2()
    elif diceX == 2 and diceY == 4:
        WM=2
        wonX2()
    elif diceX == 3 and diceY == 3:
        WM=3
        wonX3()
    elif diceX == 3 and diceY == 6:
        WM=2
        wonX2()
    elif diceX == 4 and diceY == 2:
        WM=2
        wonX2()
    elif diceX == 4 and diceY == 4:
        WM=2
        wonX2()
    elif diceX == 5 and diceY == 1:
        WM=2
        wonX2()
    elif diceX == 5 and diceY == 3:
        WM=2
        wonX2()
    elif diceX == 6 and diceY == 2:
        WM=3
        wonX3()
    elif diceX == 6 and diceY == 6:
        WM=7
        wonX7()
    else:
        WM=0
        lost()

def printGrid3(): # This function will draw the grid.
    text_file = open("grid3.txt", "r") # Opens grid2.txt in read mode.
    print(text_file.read(),"\n") # The grid is already drawn in the file grid3.txt.
    text_file.close() # Closes the text file that was in read mode.

def grid3GameOutcome(): # This function is to determine whether the user win the game or not
    global diceX, diceY,WM # I made this variable global so i can use it outside the function.
    if diceX == 1 and diceY == 1: # Calls the respective winX function when won. Calls the lost function if lost.
        WM=7
        wonX7() 
    elif diceX == 1 and diceY == 6:
        WM=3
        wonX3() 
    elif diceX == 2 and diceY == 5:
        WM=7
        wonX7() 
    elif diceX == 3 and diceY == 1:
        WM=7
        wonX7()
    elif diceX == 3 and diceY == 3:
        WM=3
        wonX3()
    elif diceX == 4 and diceY == 3:
        WM=3
        wonX3() 
    elif diceX == 5 and diceY == 4:
        WM=3
        wonX3()
    elif diceX == 6 and diceY == 2:
        WM=3
        wonX3() 
    elif diceX == 6 and diceY == 6:
        WM=7
        wonX7() 
    else:
        WM=0
        lost() # Calls lost function if the user does not get any of those above.
   

def wonX2(): # This function multiply the betAmount 2 times if the player got x2 multiplier.
    global betAmount,cashWon
    cashWon = int(betAmount * 2)
    print("\tCongratulations! You have won twice the amount you bet!\n\tYou receive ${}!\n".format(cashWon))

def wonX3():  #This function multiply the betAmount 3 times if the player got x3 multiplier.
    global betAmount,cashWon
    cashWon = int(betAmount * 3)
    print("\tCongratulations! You have won triple the amount you bet!\n\tYou receive ${}!\n".format(cashWon))

def wonX7():  #This function multiply the betAmount 7 times if the player got x7 multiplier.
    global betAmount,cashWon
    cashWon = int(betAmount * 7)
    print("\tCongratulations! You hit the jackpot! You have won x7 the amount you bet!\n\tYou receive ${}!\n".format(cashWon))

def lost(): # This function announce to the player that they lost the game.
    global cashWon
    cashWon = 0
    print("\tSorry! You have lost the amount you bet. Better luck next time!")

def backToMainMenu(): # This function calls the main function.
    pressEnter = input("\tPress 'Enter' to return to the main menu.. ")
    main()

def gameDetails(): # This function gives general idea about the game.
    cls() # Clears the screen.
    print("\n\t=========================")
    print("\t\t ABOUT")
    print("\t=========================\n")
    print("\tHabbo's Grabber is a game of chance in Habbo. Players are required to roll")
    print("\tthe two dices which correlate to a representation of a coordinate grid.")
    print("\tThe dices will roll a number ranging from 1 to 6 respectively. Typically,")
    print("\tthe grid is 6x6 spaces with scattered prizes and blank spaces throughout.")
    print("\tHowever, other variations of grid size are used such as 3x3.\n")
    print("\t=========================")
    print("\t\tDIRECTION")
    print("\t=========================\n")
    print("\tRoll the two dices. The two dices relate to coordinates on the grid. If the")
    print("\tsquare has any prizes on it, such as x2, you win twice the amount you bet.")
    print("\tIf the square is blank, you lose the credits that you risked to play.\n")

def generateDices(): # This function gets the betAmount and then generates the diceX and the diceY to determine after whether the player won or lost the game.
    global betAmount
    cls() # Clears the screen.
    print("\n\t==============================")
    print("\tHABBO GRABBER - GAME ON (3/3)")
    print("\t==============================")
    betAmount = int(input("\tEnter the amount you want to bet ($): "))
    generateDiceX() # Call generateDiceX function to generate a number from a dice representing x-axis.
    generateDiceY() # Call generateDiceY function to generate a number from a dice representing y-axis.
    print("\tThe coordinate on the grid is ({}, {}).".format(diceX, diceY)) # To print the user's coordinate on the grid.  

def gridSelection(): # Gives the player the opportunity to choose which grid he wants to bet on.
    cls() # Clear the screen.
    print("\n\t=====================================")
    print("\tHABBO GRABBER - GRID SELECTION (2/3)")
    print("\t=====================================")
    print("\t1. LOW RISK, LOW RETURN")
    print("\t2. MEDIUM RISK, MEDIUM RETURN")
    print("\t3. HIGH RISK, HIGH RETURN")
    print("\t4. BACK\n")

    gridChoice = int(input("\tEnter your choice: "))
    while gridChoice < 1 or gridChoice > 4: # Making sure that the choice is within the limits.
        gridChoice = int(input("\tEnter your choice: "))
                
    if gridChoice == 1: # Low Risk, Low Return game mode
        generateDices()
        printGrid1()
        pressEnter = input("\tPress 'Enter' to see the result! ") # I used this pressEnter all over the code to help the user understand every step of the game.
        grid1GameOutcome()
        record("Low")
        backToMainMenu()
                    
    elif gridChoice == 2: # Medium Risk, Medium Return game mode
        generateDices()
        printGrid2()
        pressEnter = input("\tPress 'Enter' to see the result! ") 
        grid2GameOutcome()
        record("Medium")
        backToMainMenu()

    elif gridChoice == 3: # High Risk, High Return game mode
        generateDices()
        printGrid3()
        pressEnter = input("\tPress 'Enter' to see the result! ")
        grid3GameOutcome()
        record("High")
        backToMainMenu()

    elif gridChoice == 4:
        cls() # Clears the screen
        selectOrPreview() # Goes back

def gridPreview(): #This function shows the player the grids he wants to check.
    cls() # Clear the screen
    print("\n\t========================================")
    print("\tHABBO GRABBER - GRID PREVIEW SELECTION")
    print("\t========================================")
    print("\t1. LOW RISK, LOW RETURN")
    print("\t2. MEDIUM RISK, MEDIUM RETURN")
    print("\t3. HIGH RISK, HIGH RETURN")
    print("\t4. BACK\n")
    gridPreviewChoice = int(input("\tEnter your choice: "))
    
    while gridPreviewChoice < 1 or gridPreviewChoice > 4: # Making sure that the choice is within the limits.
        gridPreviewChoice = int(input("\tEnter your choice: "))

    if gridPreviewChoice == 1:
        printGrid1()
        pressEnter = input("\tPress 'Enter' to return back to the grid preview selection.. ")
        gridPreview() # Go back to to the grid preview selection

    elif gridPreviewChoice == 2:
        printGrid2()
        pressEnter = input("\tPress 'Enter' to return back to the grid preview selection.. ")
        gridPreview() # Go back to to the grid preview selection

    elif gridPreviewChoice == 3:
        printGrid3()
        pressEnter = input("\tPress 'Enter' to return back to the grid preview selection.. ")
        gridPreview() # Go back to to the grid preview selection

    elif gridPreviewChoice == 4:
        cls() # Clears the screen
        selectOrPreview() # Go back 

def selectOrPreview():
    cls() # Clears the screen
    print("\n\t==========================================")
    print("\tHABBO GRABBER - SELECT/PREVIEW GRID (1/3)")
    print("\t==========================================")
    print("\t1. SELECT GRID")
    print("\t2. GRID PREVIEW")
    print("\t3. BACK\n")
    selectOrPreviewChoice = int(input("\tEnter your choice: "))
    while selectOrPreviewChoice < 1 or selectOrPreviewChoice > 3: # Making sure that the choice is within the limits.
        selectOrPreviewChoice = int(input("\tEnter your choice: "))

    if selectOrPreviewChoice == 1:        
        gridSelection() # Goes to grid selection

    elif selectOrPreviewChoice == 2:
        gridPreview() # Goes to grid preview selection

    elif selectOrPreviewChoice == 3:
        main() # Return back to main menu

def playersRecord(): # This function shows the player the past records of the games from before.
    cls() # Clears the screen
    print("\t================================")
    print("\t\tPLAYERS' RECORD")
    print("\t================================\n")
    print("\t-----------------------------------------------------------------------------")
    print("\tSession ID\tGame Mode\tBet Amount($)\t Win Multiplier\t  Cash Won($)")
    print("\t-----------------------------------------------------------------------------")
    text_file = open("playersRecord.txt","r")
    lines = text_file.readlines()
    for line in lines :
        line = line.strip().split("\t") # Turns the line from a string into a list of the details that I want to show the player about the last games.
        print("\t   {}\t\t{}\t\t     {}\t\t{}\t    {}".format(line[0],line[1],line[2],line[3],line[4]))
    print("\t-----------------------------------------------------------------------------\n")
    
def record(Mode):  # I call this function after the end of every bet to store the game details into the file playersRecord.txt, to check later.
    text_file = open("playersRecord.txt","r") # Opens playerRecords.txt in read mode.
    lines = text_file.readlines()
    lines = [line.strip() for line in lines]
    if lines == []: # This is for the first entry I use the id 1.
        session_id = 1
    else: # After the first entry I use the last id to determine the id I need to use.
        session_id = int(lines[-1].split("\t")[0]) + 1 # This extracts the last id used and add 1 to determine the next id.
    text_file.close() # Closes the text file that was in read mode.
    text_file = open("playersRecord.txt","a") # I used the file in append mode to maintain the previous data and add the current game.
    line = "\t" + "\t".join([str(session_id), Mode, str(betAmount), str(WM), str(cashWon)]) + "\n" # Adds the details of this game in a new line.
    text_file.write(line)
    text_file.close() # Closes the text file that was in append mode.
    
def main():
    cls() # Clear screen
    print("\n\t==========================")
    print("\tHABBO GRABBER - MAIN MENU")
    print("\t==========================")
    print("\t1. PLAY NOW")
    print("\t2. GAME DETAILS")
    print("\t3. PLAYERS' RECORD")
    print("\t4. EXIT\n")
    menuChoice = int(input("\tEnter your choice: "))
    while menuChoice < 1 or menuChoice > 4: # Making sure that the choice is within the limits.
        menuChoice = int(input("\tEnter your choice: "))
        
    if menuChoice == 1: # Play the game
        selectOrPreview()

    elif menuChoice == 2: # Read game details
        gameDetails()
        backToMainMenu()
    elif menuChoice == 3: # Access the players' record
        playersRecord()
        backToMainMenu()

    elif menuChoice == 4: # Exit the program     
        exit()
                         
if __name__ == "__main__":                      
    main() # Calls main function



