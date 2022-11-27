# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

*   The purpose of the Bingo program is to create and store different randomly generated bingo cards based on a users input.
*   The user will be prompted through the menu for details: card dimensions, number of cards to generate, max number on a card.
*   The user will also be able to print out cards or save them to a file.

*   A good solution will be able to:
    *   Process user input and display correct menus
    *   Generate random bingo cards (appropriate free spaces, column letters, and no repeating numbers)
    *   Print out specific cards or all cards.
    *   Save a deck (collection of cards) to a file.
    *   Clearly convey program usage through the manual instructions.
    *   Work with the test programs and pass all tests.

*   I already know how to:
    *   process user input and strings.
    *   work with multidimensional arrays (potentially useful for the Card class)
    *   format strings and create displays.

*   I might have a challenge with:
    *   Working with mutliple classes and files.
    *   Writing to files in python.

## Phase 1: System Analysis *(10%)*

### Input:
*   Input from the command line (not arguments. It uses an interactive menu)
*   Case does not matter.
*   All input must be validated (numbers, strings, letters).
*   Numbers (size of cards, numbers on cards) must be in valid range.
*   Input prompts are repeated if invalid input.

### Output:
*   Prints out a menu with correct options.
*   Randomly generated bingo card(s) that follow requirements.
*   Prints out specific card(s).

### Algorithms:
*   Bingo cards need to be generated with no repeat numbers.
*   If the program just uses the random number generator it will create cards with repeat numbers.
*   An algorithm that would solve this problem could create a list of all the possible numbers (no repeat numbers) in a card, shuffle that list, then just pop off the elements one by one to populate the card.
*   This approach would prevent repeat numbers in cards. 

## Phase 2: Design *(30%)*

### Card
*   __init__(id : int, rns : RandomNumberSet)
    *   purpose : initialize bingo card
```
def __init__(self, id, rns):
    initialize private card id
    
    shuffle rns
    intialize nums as the segments from rns (this should be all the numbers and are accessible by [x][y])
    if odd size:
        change middle value in nums to "FREE!"
```

*   id()
    *   purpose : return id
```
def id(self):
    return own id
```

*   number_at(row : int, col : int)
    *   purpose : return number at a specific spot in card
```
def number_at(row, col):
    return value of nums at index (col, row)    
```

*   __len__()
    *   purpose : return size of card
```
def __len__(self):
    return size of card (len(nums))
```

*   __str__()
    *   purpose : print out card
```
def __str__(self):
    print a neatly formatted, square bingo card
    column title letters should be printed
    numbers should be left justified
```

### Deck
*   __init__(cardSize : int, numCards : int, maxNum : int)
    *   purpose : intialize a deck with cards
```
def __init__(self, cardSize, numCards, maxNum):
    intialize cardSize as private int
    intialize numCards as private int
    intialize maxNum as private int

    create and store (numCards) in private cards list # cards are created using a RandNumberSet
```

*   __len__()
    *   purpose : return number of cards in a deck
```
def __len__(self):
    return len(cards) # or numCards
```

*   __getitem__(n : int)
    *   purpose : return card N from a deck
```
def __getitem__(self, n):
    return card with id == n
```

*   __str__()
    *   purpose : return entire deck as a string
```
def __str__(self):
    create result as empty string
    iterate over cards:
        add each str(card) to result
    return the result
```

### UserInterface

*   create_deck()
    *   purpose : create deck with user input and switch menu
```
def create_deck(self):
    get user input with get_int() to get numCards[2-8192], cardSize[3-16]
    get user input with get_int() for maxNumber

    create new deck and store it in __m_currentDeck
    switch to __deck_menu() by calling it
```

*   get_str(prompt : string)
    *   purpose : repeat until it gets a non-empty string input from user
```
def get_str(self, prompt):
    print prompt
    get user input from input()
    if input is non-empty:
        return input
    else:
        call get_str() with same prompt
```

*   get_int(prompt : string, lo : int, hi: int)
    *   purpose : return a validated integer input by user
```
def __get_int(self, prompt, lo, hi):
    print prompt
    get user input from input()
    
    if input is not an int:
        call __get_int() with same initial parameters
    
    if int(input) is in range of [low, high]:
        return int(input)
    print helpful message about range
    call __get_int() with same initial parameters # return statement will either return with correct output or it will default to repeating the prompt
```

*   print_card()
    *   purpose : prompt for a card ID and print that card from the deck
```
def __print_card(self):
    get card ID from __get_int(prompt, 1, #cards in deck)
    print out that card using the deck
```

*   save_deck()
    *   purpose : save a deck to a file
```
def __save_deck(self):
    get fileName to write to with get_str() # should just be in current working directory
    write str(m_currentDeck) to the file
```

### BAD INPUT:
*   The program will validate user input and make sure that the program only recieves correct input.
*   If the user input is invalid, the prompts will repeat until correct input is given.


## Phase 3: Implementation *(15%)*
*   Implementation went swimmingly.
*   Learned that private attributes and methods need self on the front of them to be accessible
*   One major change to design:
    *   Card class changed to get numbers from RandNumberSet using get_sements() instead of next_row()
        *   All this changed was the structure of the Card's nums list and how to access each cell in the bingo card. Originally it was [y,x]. Now it's [x,y].
*   I was stuck on get_int and get_str in the UserInterface class. My recursive design caused problem when returning values.

## Phase 4: Testing & Debugging *(30%)*
### TEST:
```
python runTests.py
test_add_options (Testing.testMenu.TestMenu)
Ensure that options can be added to a Menu ... ok
test_get_options (Testing.testMenu.TestMenu)
Ensure that menu options can be retrieved from Menus ... ok
test_is_valid_command (Testing.testMenu.TestMenu)
Ensure Menu can distinguish bad commands from the good ones ... ok
test_chCommand (Testing.testMenuOption.TestMenuOption)
Ensure each option's letter char is set correctly ... ok
test_str (Testing.testMenuOption.TestMenuOption)
Ensure the __str__ dunder works correctly ... ok
test_szDescription (Testing.testMenuOption.TestMenuOption)
Ensure each option's description is set correctly ... ok
test_getitem (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that RandNumberSet ... ok
test_len (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that a RandNumberSet's length is as expected ... ok
test_next_row (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that a RandNumberSet's .next_row() method ... ok
test_no_duplicates (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that a RandNumberSet contains no duplicates ... ok
test_freeSquares (Testing.testCard.TestCard)
Ensure that odd-sized cards have 1 "Free!" square in the center ... ok
test_id (Testing.testCard.TestCard)
Assert that each card's ID number is as expected ... ok
test_len (Testing.testCard.TestCard)
Assert that each card's size is as expected ... ok
test_no_duplicates (Testing.testCard.TestCard) ... ok
test_card (Testing.testDeck.TestDeck)
Ensure that Cards can be accessed from within a Deck ... ok
test_len (Testing.testDeck.TestDeck)
Ensure that Decks contain expected number of cards ... ok

----------------------------------------------------------------------
Ran 16 tests in 2.533s
```
*   Ran all unit tests

## BUGS
*   BUG : RandomNumberSet had repeat numbers in the set.
*   REASON : The previous programmer had assumed that range in python is exclusive of the endpoint. They added a + 1 on the endpoint to compensate for what they assumed was an endpoint exclusive range, when in reality, range is endpoint inclusive.
    *   ```self.__m_segments.append(list(range(low, high + 1)))```
*   FIX : Removed + 1 from highpoint.
    *   ```self.__m_segments.append(list(range(low, high)))```


*   BUG : Inputting a correct int after inputting an incorrect one caused an index out of range error. This was really unexpected.
*   REASON : The recursion design of the get_int get_string functions created an issue with returning a value when the function has been recursively called. In this case, this is because return only returns to the context from which it was called.
```
ID of card to print [1 - 3]:
4
Please input a number in the range [1 - 3]
ID of card to print [1 - 3]:
3
Traceback (most recent call last):
  File "src/bingo.py", line 32, in <module>
    UserInterface().run()
  File "/mnt/c/Users/camer/Documents/ComputerScience/cs1440-allen-cameron-assn4/src/UserInterface.py", line 69, in run
    self.__create_deck()
  File "/mnt/c/Users/camer/Documents/ComputerScience/cs1440-allen-cameron-assn4/src/UserInterface.py", line 93, in __create_deck
    self.__deck_menu()
  File "/mnt/c/Users/camer/Documents/ComputerScience/cs1440-allen-cameron-assn4/src/UserInterface.py", line 110, in __deck_menu
    self.__print_card()
  File "/mnt/c/Users/camer/Documents/ComputerScience/cs1440-allen-cameron-assn4/src/UserInterface.py", line 159, in __print_card
    print(self.__m_currentDeck[id])
  File "/mnt/c/Users/camer/Documents/ComputerScience/cs1440-allen-cameron-assn4/src/Deck.py", line 57, in __getitem__
    return self.__cards[n-1]
IndexError: list index out of range
```

*   example of recursion issue:
```
old code:
def __get_int(self, prompt, lo, hi):                   

        cmd = input(prompt)
        helpfulMessage = "Please input a number in the range [{low} - {high}]".format(low=lo, high=hi)
        try:
            cmd = int(cmd)
        except ValueError:
            print(helpfulMessage)
            self.__get_int(prompt, lo, hi) # RESULT OF THIS CALL IS NEVER RETURNED to print_card()

        if cmd<lo or cmd>hi:
            print(helpfulMessage)
            self.__get_int(prompt, lo, hi) # RESULT OF THIS CALL IS NEVER RETURNED to print_card()
        return cmd
```
*   This code doesn't return the result of the recursive call of get_int
*   FIX : added a return to the front of the get_int and get_str recusive calls
```
def __get_int(self, prompt, lo, hi):                   

        cmd = input(prompt)
        helpfulMessage = "Please input a number in the range [{low} - {high}]".format(low=lo, high=hi)
        try:
            cmd = int(cmd)
        except ValueError:
            print(helpfulMessage)
            return self.__get_int(prompt, lo, hi) # RESULT OF THIS CALL IS RETURNED to print_card()

        if cmd<lo or cmd>hi:
            print(helpfulMessage)
            return self.__get_int(prompt, lo, hi) # RESULT OF THIS CALL IS RETURNED to print_card()
        return cmd
``` 
    *   This means they will return a value no matter how far down in the recursion they are.

### testDeck.py changed
*   Test to see if cards are accessible from deck was changed
*   Previous:
```
self.assertIsNone(self.deck2.card(0))                  
self.assertIsNotNone(self.deck2.card(1))                 
self.assertIsNone(self.deck2.card(3))                  
```
*   Changed to:
```
self.assertIsNone(self.deck2[0])                  
self.assertIsNotNone(self.deck2[1])                 
self.assertIsNotNone(self.deck2[2])
self.assertIsNone(self.deck2[3])
```
*   REASON : My implementation of Deck has no attribute 'card'. Cards are accesible from deck[cardIndex].


### testCard.py
*   I wrote the unit tests for card to check card size, id, freesquares, and duplicate numbers
*   setUp()
*   purpose : setup cards to test
```
def setUp(self):
    intialize 4 cards to test with even and odd sizes
```
*   test_len()
*   purpose : test the length of each card
```
def test_len(self):
    assert that each of the lengths of the cards are as expected
```
*   test_id()
*   purpose : test the id of each card
```
def test_id(self):
    assert that each id from (card.id()) is as expected
```
*   test_freeSquares(self)
*   purpose : test that odd sized cards have free spaces and even cards do not.
```
def test_freeSquares(self):
    assert that odd sized cards have "FREE!" in the middle cell
    assert that even sized cards do NOT have "FREE!" in the centerish of the cards
```
*   lookForDuplicates(card : Card)
*   purpose : iterate over a cards cells and check if there are any duplicate numbers
```
def lookForDuplicates(self, card):
    intialize seenNumbers as a set
    for each cell in card, assert that the cell is not in seenNumbers (this will exit the program if there are repeats)
    append that cell to the seenNumbers set
```
*   test_no_duplicates()
*   purpose : check that there are no duplicate numbers in cards
```
def test_no_duplicates(self):
    call lookForDuplicates( card ) on 4 different cards with different sizes
```

## Phase 5: Deployment *(5%)*

*   Deployed

## Phase 6: Maintenance
### What parts of my program are hard to understand? : 
*   The hardest to read and understand part of my code is in the Card's __str()__ function. I tried to make the formatting as intuitive as possible, but it ended up just being messy. There is probably a better way to print out 2d array type object than the approach I took.
*   The Menu Option class is the most confusing for me. I mostly understand how it works, but the attribute and method names are kind of confusing. I think this is mostly due to it being converted from c++ code to python.
*   If a bug is reported in the next few months, it might take me 2 or 3 days to find the cause and fix it. Some of the code I didn't write and so it might take me a while to navigate it.

### Does my documentation make sense? :
*   My documentation is pretty good. I will be able to make sense of it in six months time and it should make sense to anyone else working on the project.

### Maintenance 
*   It will be fairly easy to add a new feature to this program in a year. The design of the program seprates each part of the problem into classes. This makes it easier to implement new classes and functionality and integrate it into the project.
*   The program will continue to work even after upgrading hardware, operating system, and python version.