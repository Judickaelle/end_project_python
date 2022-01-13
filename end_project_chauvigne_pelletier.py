# end_project
# -----------------------------------------------------
#                        IMPORT 
# -----------------------------------------------------
from pathlib import Path
from dfr import DataFileReader   # get access to data file reader
from datetime import date
import time
import random

# -----------------------------------------------------
#                      CLASS
# -----------------------------------------------------

# ----------------   CLASS FOR MEMORY  ----------------
# ----------------------- Cards -----------------------
class Card:
    nCard = 0

    def __init__(self):
        self._find = 0
        Card.nCard += 1

    def SetFind(self, find):
        self._find = find

    def GetFind(self):
        return self._find

    def GetSymbol(self):
        return self._symbol

    def GetSymbolN(self, n):
        return self._symbol[n]

# ------------------ Deck of Cards ------------------
class DeckCard(Card):
    def __init__(self, symbol="AAAA"):
        Card.__init__(self)
        self._symbol = symbol
        if self._symbol[2] == "♥" or self._symbol[2] == "♦":
            self._color = "red"
        else:
            self._color = "black"

    def GetCouleur(self):
        return self._color


def GetCouleur():
    return 0

# --------------- Deck of LetterCards ---------------
class LetterCard(Card):
    def __init__(self, symbol="AAAA"):
        Card.__init__(self)
        self._symbol = symbol

# ------------------ Memory ------------------
class Memory:
    def __init__(self):

        # Table of cards
        
        self._tabCardDeck = (" 1♥ ", " 1♠ ", " 1♦ ", " 1♣ ", " 7♥ ", " 7♦ ",
                             " 7♠ ", " 7♣ ", " 8♥ ", " 8♦ ", " 8♠ ", " 8♣ ",
                             " 9♥ ", " 9♦ ", " 9♠ ", " 9♣ ", "10♥ ", "10♦ ",
                             "10♠ ", "10♣ ", " V♥ ", " V♦ ", " V♠ ", " V♣ ",
                             " D♥ ", " D♦ ", " D♠ ", " D♣ ", " R♥ ", " R♦ ", " R♠ ", " R♣ ")

        self._tabLetter = ("AAAA", "AAAA", "BBBB", "BBBB", "CCCC", "CCCC", "DDDD", "DDDD", "EEEE", \
                           "EEEE", "FFFF", "FFFF", "GGGG", "GGGG", "HHHH", "HHHH", "IIII", "IIII", \
                           "JJJJ", "JJJJ", "KKKK", "KKKK", "LLLL", "LLLL", 'MMMM', "MMMM", "NNNN", \
                           "NNNN", "OOOO", "OOOO", "PPPP", "PPPP", "QQQQ", "QQQQ", "RRRR", "RRRR")

        self._tabLetterHard = ("AAAA", "AAAA", "AAAA", "AAAA", "BBBB", "BBBB", "BBBB", "BBBB", "CCCC", "CCCC", "CCCC", "CCCC", \
                               "DDDD", "DDDD", "DDDD", "DDDD", "EEEE", "EEEE", "EEEE", "EEEE", "FFFF", "FFFF", "FFFF", "FFFF", \
                               "GGGG", "GGGG", "GGGG", "GGGG", "HHHH", "HHHH", "HHHH", "HHHH", "IIII", "IIII", "IIII", "IIII")

        # initialization of the table of card
        self._tabCard = []

        # initialization of variables
        self._ended = None
        self._choice = 0
        self._nCard = 0
        self._difficulty = 0
        self._select = None
        self._select2 = None
        self._select3 = None
        self._select4 = None
        self._pairFound = 0
        self._try = 0;

    def memoryMenu(self):
        print("\n--------------♥♠♦♣ Memory menu ♥♠♦♣---------------")

        self._choice = int(self.typeCardChoice())  # Choice of the type of card

        self._difficulty = self.difficultyChoice()

        self._nCard = self.numberOfCardChoice()  # Choice of the number of cards

        self.CreationTab()  # Generation of the deck

        random.shuffle(self._tabCard)  # random shuffle of the deck

        self.Game()  # Start the game

    def CreationTab(self):

        # Creation of the deck
        if self._choice == 1:
            for i in range(0, self._nCard):
                self._tabCard.append(DeckCard(self._tabCardDeck[i]));

        if self._choice == 2:
            if self._difficulty == 1:
                for i in range(0, self._nCard):
                    self._tabCard.append(LetterCard(self._tabLetter[i]));
            else:
                for i in range(0, self._nCard):
                    self._tabCard.append(LetterCard(self._tabLetterHard[i]));

        # Display the grid
        for i in range(0, self._nCard):
            if i < 10:
                print("0", end='')
            print(str(i) + "[****] ", end=' ')
            if (i + 1) % 4 == 0 and i != 0:
                print()

    def difficultyChoice(self):
        while True:
            try:
                print("\nwith what difficulty do you want to play ? (1: Normal, 2: Hard):")
                self._difficulty = int(input())

                # Verification of the value
                if self._difficulty != 1 and self._difficulty != 2:
                    print("\nPlease enter 1 or 2")
                else:
                    if self._difficulty == 1:
                        print("\nDifficulty normal : you need to find pairs")
                        return int(self._difficulty)
                    if self._difficulty == 2:
                        print("\nDifficulty hard : you need to find quadruple")
                        return int(self._difficulty)

            # if not a number
            except ValueError:
                print("\nPlease enter 1 or 2")

    def typeCardChoice(self):

        valideChoice = False
        # the user will be asked to choose what memory game he wants to play
        while (not valideChoice):
            try:
                memoryMenuChoice = int(input("\nPlease choose a valid item : \
                        \n1- Classical deck of cards (A♠, R♥...)\
                        \n2- Letter deck of card\
                        \n3- Go back\
                        \n4- Quit\
                        \n\nPlease enter your choice number : "))
                valideChoice = (1 <= memoryMenuChoice <= 4)
                if not valideChoice:
                    print("\nThe item you choosen does not exist")
                    time.sleep(1)
            except(ValueError):
                print("\n***********An error occurs, please make another choice**********")
                time.sleep(1)
        match memoryMenuChoice:
            case 1:
                print("\n Classical deck of cards")
                return 1
            case 2:
                print("\nLetter deck of cardy")
                return 2
            case 3:
                mainMenu()
            case 4:
                print("\nWe hope to see you soon again")
                time.sleep(1.5)
                quit()
            case _:
                print("\nDidn't match a case")

    # Choose of the number of cards
    def numberOfCardChoice(self):

        while True:
            try:
                print("\nWith how many cards do you want to play ? (min : 8, max: 32, even number)")
                self._nCard = int(input())

                # Verification of the value
                if self._nCard < 8 or self._nCard > 32 or self._nCard % (self._difficulty*2) != 0:
                    print("\nPlease enter an even value between 8 and 32")
                else:
                    return int(self._nCard)

            # if not a number
            except ValueError:
                print("\nPlease enter an even value between 8 and 32")

    # Select a card
    def InputCard(self):
        while True:
            try:
                print("Enter card number (-1 to exit)", end=" : ")
                select = int(input())

                # Verification of the value
                if select >= -1 and select < self._nCard and self._tabCard[select].GetFind() == 0:
                    return select
                else:
                    print("incorrect value")

            # if not a number
            except ValueError:
                print("the number must be between 0 and " + str(self._nCard))

    # Display cards function
    def Display(self):
        for i in range(0, self._nCard):

            # Add 0 before small number
            if (i < 10):
                print("0", end='')

            # print symbol if selected
            if (i == self._select or i == self._select2 or i == self._select3 or i == self._select4):
                print(str(i) + "[" + self._tabCard[i].GetSymbol() + "] ", end=' ')

            # print symbol if pair already found
            elif (self._tabCard[i].GetFind() == 1):
                print(str(i) + "[" + self._tabCard[i].GetSymbol() + "] ", end=' ')

            # Else hide symbol
            else:
                print(str(i) + "[****] ", end=' ')

            # line break every 4 displays
            if ((i + 1) % 4 == 0 and i != 0):
                print()

    def Game(self):
        # Loop if there are still pairs not found
        while (self._pairFound != (self._nCard / 2)):
            print("\n")
            self._select = None
            self._select2 = None
            self._select3 = None
            self._select4 = None

            self._ended = False

            print("CARD N°1 :")
            self._select = self.InputCard()  # input first card

            if (self._select == -1):  # exit if -1
                break;

            self.Display()  # Display table

            print("\n")
            print("CARD N°2 :")

            while (True):
                self._select2 = self.InputCard()  # input second card

                # verify input
                if self._select2 != self._select:
                    break;
                else:
                    print("please select two different cards")

            if (self._select2 == -1):  # exit if -1
                break;

            self.Display()

            if self._difficulty == 2:
                print("\n")
                print("CARD N°3 :")

                while (True):
                    self._select3 = self.InputCard()  # input second card

                    # verify input
                    if self._select3 != self._select and self._select3 != self._select2:
                        break;
                    else:
                        print("please select two different cards")

                if (self._select3 == -1):  # exit if -1
                    break;

                self.Display()  # Display table

                print("\n")
                print("CARD N°4 :")

                while (True):
                    self._select4 = self.InputCard()  # input second card

                    # verify input
                    if self._select4 != self._select and self._select4 != self._select2 and self._select4 != self._select3 :
                        break;
                    else:
                        print("please select two different cards")

                if (self._select4 == -1):  # exit if -1
                    break;

                self.Display()  # Display table

            self._try += 1;  # count number of try

            # Check if pair
            if self._difficulty == 1:
                if (self._tabCard[self._select].GetSymbolN(1) == self._tabCard[self._select2].GetSymbolN(1) and
                        self._tabCard[self._select].GetCouleur() == self._tabCard[self._select2].GetCouleur()):
                    self._tabCard[self._select].SetFind(1)
                    self._tabCard[self._select2].SetFind(1)
                    self._pairFound += 1

            # Check if quadriple
            if self._difficulty == 2:
                if (self._tabCard[self._select].GetSymbolN(1) == self._tabCard[self._select2].GetSymbolN(1) and
                        self._tabCard[self._select2].GetSymbolN(1) == self._tabCard[self._select3].GetSymbolN(1) and
                        self._tabCard[self._select3].GetSymbolN(1) == self._tabCard[self._select4].GetSymbolN(1)):
                    self._tabCard[self._select].SetFind(1)
                    self._tabCard[self._select2].SetFind(1)
                    self._tabCard[self._select3].SetFind(1)
                    self._tabCard[self._select4].SetFind(1)
                    self._pairFound += 2
            # Check if all pair are found
            if (self._pairFound == (self._nCard / 2)):
                print("\n\n==============================================")
                print("            Congratulation !")
                print("            You won with " + str(self._try) + " try")
                print("==============================================")

                playerName = input("Please enter your name to save your result : ")
                saveGame(playerName, "Memory", "difficulty", int(self._try))


# -----------------------------------------------------
#                      FUNCTIONS
# -----------------------------------------------------


# ----------------- mainMenu function-------------------
def mainMenu():
    print("\n-------------------   Main menu   -------------------")
    valideChoice = False
    # the user will be asked to choose what he wants to do
    while (not valideChoice):
        try:
            mainMenuChoice = int(input("\nPlease choose a valid item : \
            \n1- Memory Game\
            \n2- Statistic\
            \n3- Quit\
            \n\nPlease enter your choice number : "))
            valideChoice = (1 <= mainMenuChoice <= 3)
            if not valideChoice:
                print("\nThe item you choosen does not exist")
                time.sleep(1)
        except(ValueError):
            print("\n***********An error occurs, please make another choice**********")
            time.sleep(1)
    # according to the user answer the programm continue running
    match mainMenuChoice:
        case 1:
            newMemory = Memory()  # create an instance of the memory class
            newMemory.memoryMenu()  # start the memory menu
        case 2:
            print("\nStatistic Lobby")
        case 3:
            print("\nWe hope to see you soon again")
            time.sleep(1.5)
            quit()
        case _:
            print("\nDidn't match a case")

# -------------------- Save game function ----------------------
def saveGame(playerName, game, difficulty, score):
    myfilepath = Path('stat.txt')
    try:
        myfilepath.touch(exist_ok=True)  #If we set the exist_ok as True, the function will do nothing if the file exists.
    except(FileExistsError):
        my_file = open("stat.txt", "a+")    #Create the file if it does not exist and then open it in append mode
        my_file.write("Player Name  Game    Difficulty  Number of try   Date\n")
        my_file.close

    my_file = open("stat.txt", "a")
    today = date.today()
    my_file.write(playerName,"\t",game,"\t",difficulty,"\t",score,"\t",today,"\n") 
    my_file.close


# ---------------- Read statistic file function ------------------
def readStatisticFile():
    dfr = DataFileReader("waterlevel.txt", sep="\t", header=True)
    header = dfr.get_header()
    print(header)

    i=0
    while True:
        content = dfr.get_data()
        print(i,":   ",content)
        i=i+1

# -----------------------------------------------------
#                          MAIN
# -----------------------------------------------------

try:
    print("-----------------------------------------------------\n\
                    WELCOMME GAMER\n\
-----------------------------------------------------")
    mainMenu()
except(KeyboardInterrupt):
    print("\nWe hope to see you soon again")
    time.sleep(1.5)  # the programm freeze during 1.5s
