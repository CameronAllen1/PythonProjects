class Menu():  	    	       
    """  	    	       
    Present a Menu made of of MenuOptions to a user, and continue to prompt until they provide valid input  	    	       

    When the user's selection is alphabetic, it is matched without regard to case;  	    	       
    both upper- and lower-case letters are accepted  	    	       
    """  	    	       

    def __init__(self, szHeader):  	    	       
        """  	    	       
        Create an empty Menu  	    	       

        Takes a string describing the Menu as input  	    	       
        """  	    	       
        self.__m_szHeader = szHeader  	    	       
        self.__m_options = []  	    	       

    def __iadd__(self, option):  	    	       
        """  	    	       
        Append an option to the Menu  	    	       

        This method was called `operator+` in the C++ version  	    	       

        Be careful: No check is made for a duplicate MenuOption command  	    	       
        """  	    	       
        self.__m_options.append(option)  	    	       
        return self  	    	       

    def __getitem__(self, nIdx):  	    	       
        """  	    	       
        Return a MenuOption  	    	       

        This method was called `operator[]` in the C++ version  	    	       

        Retrieve an option from the menu with the indexing operator []  	    	       
        """  	    	       
        if 0 <= nIdx < len(self):  	    	       
            return self.__m_options[nIdx]  	    	       
        else:  	    	       
            raise IndexError  	    	       

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the number of MenuOptions contained in this Menu  	    	       

        This method was called `length` in the C++ version, and was meant to be explicitly called  	    	       
        """  	    	       
        return len(self.__m_options)  	    	       

    def bIsValidCommand(self, chCommand):  	    	       
        """  	    	       
        Return a Boolean: whether a command is contained in our list of MenuOptions  	    	       

        Consider upper-case options the same as lower-case  	    	       
        """  	    	       
        for i in range(len(self)):  	    	       
            if chCommand.upper() == self[i].chCommand().upper():  	    	       
                return True  	    	       
        return False  	    	       

    def prompt(self):  	    	       
        """  	    	       
        Return None: Display the menu and take a command from the user  	    	       

        The menu is repeated until the user provides a recognized command  	    	       
        """  	    	       
        while True:  	    	       
            options = []  	    	       

            print(f"\n{self.__m_szHeader} menu:")  	    	       
            for i in range(len(self)):  	    	       
                option = self[i]  	    	       
                if option is not None:  	    	       
                    print(option)  	    	       
                    options += option.chCommand()  	    	       

            print(f"\nEnter a {self.__m_szHeader} command ({', '.join(options)})")  	    	       
            command = input()  	    	       
            if self.bIsValidCommand(command):  	    	       
                return command  	    	       
            else:  	    	       
                print(f"'{command.strip()}' is not a valid option")  	    	       
