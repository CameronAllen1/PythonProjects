# Bingo! User Manual  	         	  

## Running The Program
*	Run the program from the main project directory with the command ```python src/bingo.py```


## Menu And Functionality
*	Upon running the program, you will be presented with a "Main Menu" that has two options:
	*	C - Create a new deck
	*	X - Exit the program
*	In order to choose an option, type the letter of the option you wish to choose and press enter.
*	All input in the program is case insensitive, meaning your input can be upper or lower case.
*	If you enter invalid input at any point, the prompt will repeat.

*	If you choose "Create a new deck" you will be prompted to input:
*	Card Size
	*	This card size must be a number within the specified range [3-16].
*	Max Number
	*	This must be a number within the specified range.
*	Number of Cards
	*	This must be a number within the specified range [2-8192].

*	After these prompts, a deck will be created and you will be presented with a "Deck Menu" that has four options:
	*	P - Print a card to the screen
	*	D - Display the whole deck to the screen
	*	S - Save the whole deck to a file
	*	X - Return to the Main menu

*	If you choose "Print a card to the screen," you will be prompted to input an id for which card to print out.
*	If you choose "Display the whole deck to the screen," the program will print the whole deck to the screen.
*	If you choose "Save the whole deck to a file," you will be prompted to input a file name to save the deck to. (Note: the file will be saved relative to the directory you ran the program from)
*	If you choose "Return to the Main menu," you will be returned to the Main Menu. (Note: this will destroy the deck you just created!)

*	If you wish to force exit the program, simply press ctrl-c.

## Common Errors and How to Fix Them
*	Inputs are not being accepted :
	*	This is most likely due to incorrect input. 
	*	Make sure that your input is the right type for the prompt (numbers, letters).
	*	Make sure that there is no extra whitespace when inputting numbers.
	*	Make sure that number inputs are within specified range.

*	Stuck on prompt :
	*	If you are stuck and cannot progress past a prompt for whatever reason, you can exit the program using ctrl-c.
	*	Note : this will get rid of any unsaved deck and return you to the terminal.

