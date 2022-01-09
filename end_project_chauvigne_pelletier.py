#end_project
import time

def mainMenu() :
    valideChoice = False
    while(not valideChoice):
        try :
            mainMenuChoice = int(input("\nPlease choose a valid item : \
            \n1- Memory Game\
            \n2- Statistic\
            \n3- Quit\
            \n\nPlease enter your choice number : "))
            valideChoice = (mainMenuChoice == 1 or mainMenuChoice == 2)
        except(ValueError):
            print("\n***********An error occurs, please make another choice**********")
            time.sleep(1)

######################################################
##################### MAIN ###########################
######################################################

try :
    print("________________WELCOMME_GAMER________________")
    mainMenu()
except(KeyboardInterrupt):
    print("\nWe hope to see you soon again")
    time.sleep(1.5) #the programm will stop after 1.5s
