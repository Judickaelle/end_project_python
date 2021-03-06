# end_project
# -----------------------------------------------------
#                        IMPORT 
# -----------------------------------------------------
from datetime import date
import time
import random
import json

# -----------------------------------------------------
#                   GLOBAL VARIABLE 
# -----------------------------------------------------
press_enter = ("\nPress Enter to continue")
dash = '-' * 60

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

# --------------- Deck of LetterCards ---------------
class LetterCard(Card):
    def __init__(self, symbol="AAAA"):
        Card.__init__(self)
        self._symbol = symbol

    def GetCouleur(self):
        return 0

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
        self._difficultyName = ""
        self._select = None
        self._select2 = None
        self._select3 = None
        self._select4 = None
        self._pairFound = 0
        self._try = 0;

    def memoryMenu(self):
        print("\n{:-^60}".format(" ♥♠♦♣ Memory menu ♥♠♦♣ "))
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
                if self._difficulty != 1 and self._difficulty != 2:                     # Verification of the value
                    print("\nPlease enter 1 or 2")
                else:
                    if self._difficulty == 1:
                        print("\nDifficulty normal : you need to find pairs")
                        self._difficultyName = "Normal"
                        return int(self._difficulty)
                    if self._difficulty == 2:
                        print("\nDifficulty hard : you need to find quadruple")
                        self._difficultyName = "Hard"
                        return int(self._difficulty)
            except ValueError:                                                              # if not a number
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
                print("\n{:*^60}".format(" An error occurs, please make another choice "))
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
    
    def numberOfCardChoice(self):                                                                   # Choose of the number of cards
        while True:
            try:
                print("\nWith how many pairs do you want to play ? (min : 4, max: 16, even number if hard mode)")
                self._nCard = int(input())
                if self._nCard < 4 or self._nCard > 16 or self._nCard % (self._difficulty) != 0:    # Verification of the value
                    print("\nPlease enter an even value between 4 and 16")
                else:
                    return 2*int(self._nCard)  
            except ValueError:                                                                      # if not a number
                print("\nPlease enter an even value between 4 and 16")

    def InputCard(self):                                                                            # Select a card
        while True:
            try:
                print("Enter card number (-1 to exit)", end=" : ")
                select = int(input())
                if select >= -1 and select < self._nCard and self._tabCard[select].GetFind() == 0:   # Verification of the value
                    return select
                else:
                    print("incorrect value")
            except ValueError:                                                                      # if not a number
                print("the number must be between 0 and " + str(self._nCard))

    # Display cards function
    def Display(self):
        for i in range(0, self._nCard):
            if (i < 10):                                    # Add 0 before small number
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
                    print('\n Well done !!')

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
                    print('\n Well done !!')
            
            # Check if all pair are found
            if (self._pairFound == (self._nCard / 2)):
                print(dash)
                print("{: ^60}".format("Congratulation !"))
                print("{: ^60}".format("You won with " + str(self._try) + " try"))
                print(dash)

                playerName = input("\nPlease enter your name to save your result : ")
                saveMemoryGame(playerName, self._difficultyName, int(self._nCard/2),self._try)
                mainMenu()

# -----------------------------------------------------
#                      FUNCTIONS
# -----------------------------------------------------
# ----------------- mainMenu function------------------
def mainMenu():
    print("\n{:-^60}".format(" Main menu "))
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
            print("\n{:*^60}".format(" An error occurs, please make another choice "))
            time.sleep(1)
    # according to the user answer the programm continue running
    match mainMenuChoice:
        case 1:
            newMemory = Memory()  # create an instance of the memory class
            newMemory.memoryMenu()  # start the memory menu
        case 2:
            statisticMenu()
        case 3:
            print("\nWe hope to see you soon again")
            time.sleep(1.5)
            quit()
        case _:
            print("\nDidn't match a case")
            
#-----------------   Statistic menu   -----------------
def statisticMenu():
    print("\n{:-^60}".format(" Statistic menu "))     
    valideChoice = False
    # the user will be asked to choose what memory game he wants to play
    while (not valideChoice):
        try:
            statisticMenuChoice = int(input("\nPlease choose a valid item : \
                    \n1- Memory best score\
                    \n2- Your statistics\
                    \n3- Go back\
                    \n4- Quit\
                    \n\nPlease enter your choice number : "))
            valideChoice = (1 <= statisticMenuChoice <= 4)
            if not valideChoice:
                print("\nThe item you choosen does not exist")
                time.sleep(1)
        except(ValueError):
            print("\n{:*^60}".format(" An error occurs, please make another choice "))
            time.sleep(1)
    match statisticMenuChoice:
        case 1:
            getMemoryStat()
            statisticMenu()
        case 2:
            playerName = input("\n(Case SenSiTive !) Please enter your name : ")
            getPlayerStat(playerName)
            statisticMenu()
        case 3:
            mainMenu()
        case 4:
            print("\nWe hope to see you soon again")
            time.sleep(1.5)
            quit()
        case _:
            print("\nDidn't match a case")       

# -------------------- Save game function ----------------------
def saveMemoryGame(playerName, difficulty, pairsNumber, score):
    game = "Memory"
    try:        
        playersStat_file = open("playersStat.json", "r")            #opening the file
        gameStat_file = open("gameStat.json", "r")
        playersRecord = json.loads(playersStat_file.read())         #getting the data from the file and storing them into a dictionary
        gameRecord = json.loads(gameStat_file.read())
        playersStat_file.close()                                    #closing the file
        gameStat_file.close()
    except(FileNotFoundError):                                      #if the file does not exist
        gameRecord = {}                                             #create the dictionary from scratch
        playersRecord = {}

    today = date.today()                                            #get the date of today
    new_player_record = (game, difficulty, pairsNumber, score, str(today))       #the new tuple to register
    new_game_record = (playerName, difficulty, pairsNumber, score, str(today))

    #store the data with the player name as key
    playerData = playersRecord.get(playerName)                      #get the data from the player name
    if playerData == None:                                          #no data available
        #create a new key inside the dictionary
        data_player_list = []
        data_player_list.append(new_player_record)                  #add the new tuple inside a list
        playersRecord[playerName] = data_player_list                #store the value
    else:
        #update existing key
        playersRecord[playerName].append(new_player_record)

    playersStat_file = open("playersStat.json", "w")                #open the file to overwrite it
    json.dump(playersRecord, playersStat_file)                      #parse the data to json
    playersStat_file.close()                                        #close the file

    #store the data with the game as key
    gameData = gameRecord.get(game)                                 #get the data from the game
    if gameData == None:                                            #no data available
        #create a new key inside the dictionary
        data_game_list = []
        data_game_list.append(new_game_record)                      #add the new tuple inside a list
        gameRecord[game] = data_game_list                           #store the value
    else:
        #update existing key
        gameRecord[game].append(new_game_record)

    gameStat_file = open("gameStat.json", "w")                      #open the file to overwrite it
    json.dump(gameRecord, gameStat_file)                            #parse the data to json
    gameStat_file.close()                                           #close the file

    print("\nThe game has been successfully saved !")

# ---------------- Get Memory statistic function ------------------
def getMemoryStat():
    try:        
        a_file = open("gameStat.json", "r")         #opening the file
        gameRecord = json.loads(a_file.read())      #getting the data from the file and storing them into a dictionary
        a_file.close()                              #closing the file
    except(FileNotFoundError):                      #if the file does not exist
        print("\nPlease play at least one time to have record")
        time.sleep(1)
        mainMenu()    

    gameRecord = gameRecord.get("Memory")           #update the list to keep only Memory record
    try:
        gameRecord_normalLevel = print_memory_records(gameRecord, "Normal")
        print_total_average(gameRecord_normalLevel)
    except(ZeroDivisionError):
        print("no data\n")
    try:
        gameRecord_hardLevel = print_memory_records(gameRecord, "Hard")
        print_total_average(gameRecord_hardLevel)
    except(ZeroDivisionError):
        print("no data\n")
    return

# ------------ Get player statistic function --------------
def getPlayerStat(playerName):
    try:        
        a_file = open("playersStat.json", "r")          #opening the file
        playerRecord = json.loads(a_file.read())        #getting the data from the file and storing them into a dictionary
        a_file.close()                                  #closing the file
    except(FileNotFoundError):                          #if the file does not exist
        print("\nPlease play at least one time to have record")
        time.sleep(1)
        mainMenu()

    list_player_record = playerRecord.get(playerName)
    if list_player_record != None:                      #if the list is not empty
        previous_game = ""                              #at the begining the variables are empty
        current_game = ""
        i=0
        list_of_game = []
        #here we want to collect all the different game that the player may have played
        while i < len(list_player_record):              
            for item in list_player_record:
                current_game = item[0]
                if current_game != previous_game:
                    list_of_game.append(current_game)
                previous_game = current_game
                i=i+1
            list_of_game = remove_duplicate(list_of_game)           # we keep only once each game      
        for game in list_of_game:
            if game == "Memory":
                record_by_game = filter_list(list_player_record, game, "Normal")
                if len(record_by_game) > 0:
                    print_player_records(record_by_game)
                    print_total_average(record_by_game)
                record_by_game = filter_list(list_player_record, game, "Hard")
                if len(record_by_game) > 0:
                    print_player_records(record_by_game)
                    print_total_average(record_by_game)
            else:
                record_by_game = filter_list(list_player_record, game)
                if len(record_by_game) > 0:
                    print_player_records(record_by_game)
                    print_total_average(record_by_game)        
    else:
        print("\nThere is no record for this player\nHere are the folowwing player in the database :\n")
        print(*playerRecord.keys(), sep = ", ")          # printing the list using * and sep operator
        input(press_enter)
    return

# ------------ filter a list by given arg --------------
def filter_list(list, game, *args):
    # the list will be filtered according the different parameter selected
    # a list of record will be retrun
    new_list = [item for item in list if item[0] == game]
    for ar in args:
        new_list = [item for item in list if item[0] == game and item[1] == ar]
    # the list will be sorted first by the number of pairs and then by the score
    new_list.sort(key=lambda y: y[2])                                       # sorts the list ascending by the pair number
    
    number_pair_list = remove_duplicate([item[2] for item in new_list])     # get all the different pair number    

    # for each pair_number, a new_sub_list is created, filtered by the score and then adding to the final list
    final_filter_list = []
    for pair_number in number_pair_list:
        new_sub_list = [item for item in new_list if item[2] == pair_number]
        new_sub_list.sort(key=lambda y: y[3])                               # sorts the list ascending by the score
        final_filter_list.extend(new_sub_list)                              # add elements from one list to another list
    
    return final_filter_list    

# ---------- remove duplicate inside a list ------------
def remove_duplicate(my_list):
    # remove duplicate inside a list by transforming it into a dictionary and then convert it 
    # againt into a list
    return list(dict.fromkeys(my_list))   

# ----------------- print player records ------------------
def print_player_records(list): 
    print(dash + "-" * 8)
    print("{: ^15} {: ^15} {: ^12} {: ^10} {: ^15}".format("GAME", "DIFFICULTY", "PAIRS NUMBER", "SCORE", "DATE"))
    print(dash + "-" * 8)
    for item in list:
        print("{: ^15} {: ^15} {: ^12} {: ^10} {: ^15}".format(*item))
    return

# ----------------- print Memory records ------------------
def print_memory_records(list, difficulty):
    print(dash)
    print("{: ^60}".format("MEMORY - LEVEL : " + difficulty)) 
    print(dash)
    print("{: ^20} {: ^15} {: ^10} {: ^15}".format("PLAYER NAME", "PAIRS NUMBER", "SCORE", "DATE"))
    print(dash)
    new_list = [item for item in list if item[1] == difficulty]
     # the list will be sorted first by the number of pairs and then by the score
    new_list.sort(key=lambda y: y[2])                                       # sorts the list ascending by the pair number
    
    number_pair_list = remove_duplicate([item[2] for item in new_list])     # get all the different pair number    

    # for each pair_number, a new_sub_list is created, filtered by the score and then adding to the final list
    final_filter_list = []
    for pair_number in number_pair_list:
        new_sub_list = [item for item in new_list if item[2] == pair_number]
        new_sub_list.sort(key=lambda y: y[3])                               # sorts the list ascending by the score
        final_filter_list.extend(new_sub_list)                              # add elements from one list to another list
    for item in final_filter_list:
        print("{: ^20} {: ^15} {: ^10} {: ^15}".format(item[0], item[2], item[3], item[4]))
    return final_filter_list

# -------------- print total and average ---------------
def print_total_average(list):
    sum_score = 0
    best_score = 1000
    for item in list:
        sum_score = sum_score + item[3]
        if item[3] < best_score:
            best_score = item[3]
    average = (sum_score/len(list))
    print(dash + "-" * 8)
    print("Played : ", len(list), ("time", "times")[len(list)>1])
    print("Average = ", average)
    print("Best score = ", best_score)
    print()
    input(press_enter)
    print()
    return
                  
# -----------------------------------------------------
#                          MAIN
# -----------------------------------------------------
try:
    print(dash)
    print("{: ^60}".format("WELCOMME GAMER"))
    print(dash)
    mainMenu()
except(KeyboardInterrupt):
    print("\nWe hope to see you soon again")
    time.sleep(1.5)  # the programm freeze during 1.5s
