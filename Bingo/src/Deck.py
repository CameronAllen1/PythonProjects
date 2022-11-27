from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       

class Deck():  	    	       
    def __init__(self, cardSize, numCards, maxNum):  	    	       
        """  	    	       
        Deck constructor  	    	       
        """  	    	       
        self.__cardSize = cardSize
        self.__numCards = numCards
        self.__maxNum = maxNum 	       
        self.__cards = []
        for i in range(numCards):
            self.__cards.append( Card(i, RandNumberSet(self.__cardSize, self.__maxNum))  )

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the number of cards in this deck  	    	       

        This method was called `size` in the C++ version  	    	       
        """
        return len(self.__cards)  	    	       
	    	       

    def __getitem__(self, n): # can assume in range input because it is handled by UserInterface  	       
        """  	    	       
        Return Card N from the Deck  	    	       

        This method was called `operator[]` in the C++ version  	    	       
        """
        if (n-1<0 or n>len(self)): # do this because it could go negative, picking up the last object in the list instead of returning none
            return None

        return self.__cards[n-1]

    def __str__(self):  	    	       
        """  	    	       
        Return a string: return the entire Deck as a string  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """ 
        allCards = "" 	    	       
        for card in self.__cards:
            allCards += str(card) + "\n"
        return allCards
