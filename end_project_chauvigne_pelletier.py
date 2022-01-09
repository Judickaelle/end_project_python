#end_project
import time

def mainMenu() :
    valideChoice = False
    #the user will be asked to choose what he want to do 
    while(not valideChoice):
        try :
            mainMenuChoice = int(input("\nPlease choose a valid item : \
            \n1- Memory Game\
            \n2- Statistic\
            \n3- Quit\
            \n\nPlease enter your choice number : "))
            valideChoice = (mainMenuChoice == 1 or mainMenuChoice == 2 or mainMenuChoice == 3)
        except(ValueError):
            print("\n***********An error occurs, please make another choice**********")
            time.sleep(1)
    #according to the user answer the programm continue running
    match mainMenuChoice:
        case 1:
            print("Memory Game")
        case 2:
            print("Statistic Lobby")
        case 3:
            print("\nWe hope to see you soon again")
            time.sleep(1.5)
            quit()
        case _:
            print("Didn't match a case")    

######################################################
##################### MAIN ###########################
######################################################

try :
    print("________________WELCOMME_GAMER________________")
    mainMenu()
except(KeyboardInterrupt):
    print("\nWe hope to see you soon again")
    time.sleep(1.5) #the programm freeze during 1.5s
