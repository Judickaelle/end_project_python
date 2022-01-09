#end_project
#-----------------------------------------------------
#                        IMPORT 
#-----------------------------------------------------
import time

#-----------------------------------------------------
#                      CLASS
#-----------------------------------------------------
class Memory:
    def memoryMenu(self):
        print("-----------------   Memory menu   -----------------")
        valideChoice = False
        #the user will be asked to choose what memory game he wants to play 
        while(not valideChoice):
            try :
                memoryMenuChoice = int(input("\nPlease choose a valid item : \
                \n1- Classical deck of cards (A♠, R♥...)\
                \n2- Letter deck of card\
                \n3- Go back\
                \n4- Quit\
                \n\nPlease enter your choice number : "))
                valideChoice = (memoryMenuChoice == 1 or memoryMenuChoice == 2 
                    or memoryMenuChoice == 3 or memoryMenuChoice == 4)
                if not valideChoice:
                    print("\nThe item you choosen does not exist")
                    time.sleep(1)
            except(ValueError):
                print("\n***********An error occurs, please make another choice**********")
                time.sleep(1)
        match memoryMenuChoice:
            case 1:
                print("\n Classical deck of cards")
            case 2:
                print("\nLetter deck of cardy")
            case 3:
                mainMenu()
            case 4:
                print("\nWe hope to see you soon again")
                time.sleep(1.5)
                quit()   
            case _:
                print("\nDidn't match a case")    

#-----------------------------------------------------
#                      FUNCTIONS
#-----------------------------------------------------

#-----------------mainMenu function-------------------
def mainMenu() :
    print("-------------------   Main menu   -------------------")
    valideChoice = False
    #the user will be asked to choose what he wants to do 
    while(not valideChoice):
        try :
            mainMenuChoice = int(input("\nPlease choose a valid item : \
            \n1- Memory Game\
            \n2- Statistic\
            \n3- Quit\
            \n\nPlease enter your choice number : "))
            valideChoice = (mainMenuChoice == 1 or mainMenuChoice == 2 or mainMenuChoice == 3)
            if not valideChoice:
                    print("\nThe item you choosen does not exist")
                    time.sleep(1)
        except(ValueError):
            print("\n***********An error occurs, please make another choice**********")
            time.sleep(1)
    #according to the user answer the programm continue running
    match mainMenuChoice:
        case 1:
            newMemory = Memory() #create an instance of the memory class
            newMemory.memoryMenu() #start the memory menu
        case 2:
            print("\nStatistic Lobby")
        case 3:
            print("\nWe hope to see you soon again")
            time.sleep(1.5)
            quit()
        case _:
            print("\nDidn't match a case")    




#-----------------------------------------------------
#                          MAIN 
#-----------------------------------------------------

try :
    print("-----------------------------------------------------\n\
                    WELCOMME GAMER\n\
-----------------------------------------------------")
    mainMenu()
except(KeyboardInterrupt):
    print("\nWe hope to see you soon again")
    time.sleep(1.5) #the programm freeze during 1.5s
