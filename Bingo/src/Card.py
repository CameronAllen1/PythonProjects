class Card():  	    	       
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	    	       

    def __init__(self, id, rns):  	    	       
        """  	    	       
        Initialize a Bingo! card  	    	       
        """
        self.__id = id

        rns.shuffle()
        self.__nums = rns.get_segments() # this will get all the numbers and make them accessible by [x,y]
        
        if not(len(self.__nums)%2==0): # not even
            pos = len(self.__nums)//2 # get position of middle cell
            self.__nums[pos][pos] = "FREE!"

    def id(self):  	    	       
        """  	    	       
        Return an integer: the ID number of the card  	    	       
        """
        return self.__id

    def number_at(self, row, col):  	    	       
        return self.__nums[col][row] 

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the length of one dimension of the card.  	    	       
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	    	       

        This method was called `size` in the C++ version  	    	       
        """     
        return len(self.__nums) # both sides are same length      	    	       	    	       

    def __str__(self):  	    	       
        """  	    	       
        Return a string: a neatly formatted, square bingo card  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """  	    	       
        size = len(self) # Is it okay if I call dunder methods from own class?
        resultString = "Card #{} \n".format(self.__id + 1)
        divider ="+-----"*(size) + "+\n"
        for i in range(size): # print B I N G O
            resultString += ("   " + Card.COLUMN_NAMES[i] + "  ") # 3 spaces on left and 2 on right to space it out
        resultString += "\n"
        for col in range(size): # for all columns add a divider
            resultString += divider
            rowString = ""
            for row in range(size): # add each row to result
                if self.__nums[row][col]=="FREE!":
                    rowString += "|FREE!" # dont do any inside spacing for free squares
                else:
                    rowString += "| {:^3} ".format(self.__nums[row][col]) # center number
            
            rowString+="|\n" # add last bar on end of row
            resultString+=rowString
        resultString += divider
        return resultString #all of this stuff was just formatting the string.
