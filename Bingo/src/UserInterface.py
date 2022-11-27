from math import floor  	    	       

from Deck import Deck  	    	       
from Menu import Menu  	    	       
from MenuOption import MenuOption  	    	       

import math

class UserInterface():  	    	       
    """  	    	       
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	    	       

    Also provides methods for accepting and validating user input  	    	       
    """  	    	       

    def __init__(self):  	    	       
        self.__m_currentDeck = None  	    	       
        self.__m_menu = Menu("Main")  	    	       
        self.__m_menu += MenuOption("C", "Create a new deck")  	    	       
        self.__m_menu += MenuOption("X", "Exit the program")  	    	       

    def run(self):  	    	       
        """  	    	       
        Return None: present the main menu to the user  	    	       

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	    	       
        """  	    	       

        print("""
 ########   ####  ##    ##   ######     #######   ####
 ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
 ##     ##   ##   ####  ##  ##         ##     ##  ####
 ########    ##   ## ## ##  ##   ####  ##     ##   ##
 ##     ##   ##   ##  ####  ##    ##   ##     ##
 ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
 ########   ####  ##    ##   ######     #######   ####

    Welcome to the DuckieCorp Bingo! Deck Generator""")  	    	       

        while True:  	    	       
            command = self.__m_menu.prompt()  	    	       
            if command.upper() == "C":  	    	       
                self.__create_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __create_deck(self):  	    	       
        """  	    	       
        Return None: Create a new Deck  	    	       

        The Deck is stored in self.__m_currentDeck  	    	       

        """  	    	       
        cardSize = self.__get_int("Enter card size [3 - 16]:\n",3,16)
        
        low = 2 * (cardSize * cardSize)
        high = math.floor(3.9 * (cardSize*cardSize)) 
        maxNum = self.__get_int("Enter max number [{low} - {high}]:\n".format(low=low,high=high), low, high)  	    	       

        numCards = self.__get_int("Enter number of cards [2 - 8192]:\n", 2, 8192)

        self.__m_currentDeck = Deck(cardSize, numCards, maxNum)
        self.__deck_menu()

    def __deck_menu(self):  	    	       
        """  	    	       
        Return None  	    	       

        Present the deck menu to user until a valid selection is chosen  	    	       
        """  	    	       
        menu = Menu("Deck")  	    	       
        menu += MenuOption("P", "Print a card to the screen")  	    	       
        menu += MenuOption("D", "Display the whole deck to the screen")  	    	       
        menu += MenuOption("S", "Save the whole deck to a file")  	    	       
        menu += MenuOption("X", "Return to the Main menu")  	    	       

        while True:  	    	       
            command = menu.prompt()  	    	       
            if command.upper() == "P":  	    	       
                self.__print_card()  	    	       
            elif command.upper() == "D":  	    	       
                print(self.__m_currentDeck)  	    	       
            elif command.upper() == "S":  	    	       
                self.__save_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __get_str(self, prompt):  	    	       
        """  	    	       
        Return a string: non-empty input entered by the user  	    	       

        Take a prompt string as input  	    	       
        Repeat the prompt until a non-empty string is provided  	    	       
        """
        cmd = input(prompt)
        if len(cmd)==0:
            return self.__get_str(prompt)
        else:
            return cmd     

    def __get_int(self, prompt, lo, hi):  	    	       
        """  	    	       
        Return an integer: validated integer input by user  	    	       

        Take a prompt string, low and high integers as input  	    	       
        Repeat the prompt until an integer that is in-range is provided  	    	       
        """

        cmd = input(prompt)
        helpfulMessage = "Please input a number in the range [{low} - {high}]".format(low=lo, high=hi)
        try:
            cmd = int(cmd)
        except ValueError:
            print(helpfulMessage)
            return self.__get_int(prompt, lo, hi) # cmd is not an int. try again

        if cmd<lo or cmd>hi:
            print(helpfulMessage)
            return self.__get_int(prompt, lo, hi)
        return cmd

    def __print_card(self):  	    	       
        """  	    	       
        Return None: Print one Card from the Deck  	    	       

        Prompt user for a Card ID  	    	       
        """
        message = "ID of card to print [1 - {max}]:\n".format(max=len(self.__m_currentDeck))
        i = self.__get_int(message, 1, len(self.__m_currentDeck))
        print(self.__m_currentDeck[i])

    def __save_deck(self): # trusts the user	    	       
        """  	    	       
        Return None: Save a Deck to a file  	    	       

        Prompt user for the name of file to write the entire Deck into  	    	       
        """
        fileName = self.__get_str("Enter output file name:\n")
        file = open(fileName, 'w')
        file.write(str(self.__m_currentDeck))
        file.close()
        print("Deck saved to '{fileName}'!".format(fileName = fileName))	    	       
