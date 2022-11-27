import unittest  	    	       

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       
from random import randint
import math

class TestCard(unittest.TestCase):  	    	       

    def setUp(self):
        self.card3 = Card(1, RandNumberSet(3,3*3*3)) # RNS(card size, maxNum)
        self.card4 = Card(2, RandNumberSet(4,3*4*4))   	       
        self.card8 = Card(3, RandNumberSet(8,3*8*8))
        self.card9 = Card(4, RandNumberSet(9,3*9*9))

    def test_len(self):  	    	       
        """Assert that each card's size is as expected"""
        self.assertEqual(len(self.card3), 3) # should be size 3     	    	       
        self.assertEqual(len(self.card4), 4) # should be size 4                    
        self.assertEqual(len(self.card8), 8) # should be size 8
        self.assertEqual(len(self.card9), 9) # should be size 9                     
        self.assertNotEqual(len(self.card9), 50) # should not be size 50                   
  	    	       

    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""
        self.assertEqual(self.card3.id(), 1) # should be id 1                     
        self.assertEqual(self.card4.id(), 2) # should be id 2                    
        self.assertEqual(self.card8.id(), 3) # should be id 3
        self.assertEqual(self.card9.id(), 4) # should be id 4                     
         
        self.assertNotEqual(self.card3.id(), 4) # should not be id 4                     
   	    	       

    def test_freeSquares(self):  	    	       
        """  	    	       
        Ensure that odd-sized cards have 1 "Free!" square in the center  	    	       
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	    	       
        """
        self.assertEqual(self.card3.number_at(1,1), "FREE!") # size is 3 so 1,1 is center	    	       
        self.assertEqual(self.card9.number_at(4,4), "FREE!") # size is 9 so 4,4 is center                   
        

        # even sized cards. NOT SUPPOSED TO HAVE FREE!
        #self.cards[1] size is 4 so 1,1 is centerish. check to 2,2
        self.assertNotEqual(self.card4.number_at(1,1), "FREE!")
        self.assertNotEqual(self.card4.number_at(1,2), "FREE!")
        self.assertNotEqual(self.card4.number_at(2,1), "FREE!")       
        self.assertNotEqual(self.card4.number_at(2,2), "FREE!")

        self.assertNotEqual(self.card8.number_at(3,3), "FREE!")
        self.assertNotEqual(self.card8.number_at(3,4), "FREE!")
        self.assertNotEqual(self.card8.number_at(4,3), "FREE!")       
        self.assertNotEqual(self.card8.number_at(4,4), "FREE!")


    def lookForDuplicates(self, card): # helper function for test no duplicates
        seenNumbers = set()
        for y in range(0, len(card)):
            for x in range(0, len(card)):
                self.assertNotIn(card.number_at(x,y), seenNumbers)
                seenNumbers.add(card.number_at(x,y))

    def test_no_duplicates(self):
        self.lookForDuplicates(self.card3)
        self.lookForDuplicates(self.card4)

        self.lookForDuplicates(self.card8)
        self.lookForDuplicates(self.card9)      
        """Ensure that Cards do not contain duplicate numbers"""  	    	       
    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
