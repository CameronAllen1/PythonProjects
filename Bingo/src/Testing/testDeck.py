import unittest  	    	       
import Deck  	    	       


class TestDeck(unittest.TestCase):  	    	       
    def setUp(self):  	    	       
        size = 7  	    	       
        self.deck2 = Deck.Deck(cardSize=size, numCards=2, maxNum=3*size*size)  	    	       

        size = 16  	    	       
        self.deck16 = Deck.Deck(cardSize=size, numCards=16, maxNum=3*size*size)  	    	       
        self.deck8192 = Deck.Deck(cardSize=size, numCards=8192, maxNum=3*size*size)  	    	       

    def test_len(self):  	    	       
        """Ensure that Decks contain expected number of cards"""  	    	       
        self.assertEqual(len(self.deck2), 2)  	    	       
        self.assertEqual(len(self.deck16), 16)  	    	       
        self.assertEqual(len(self.deck8192), 8192)  	    	       

    def test_card(self):  	    	       
        """Ensure that Cards can be accessed from within a Deck"""  	    	       

        # In my implementation, an attempt to get a non-existent card results in `None`  	    	       
        # Cards are indexed by their ID number  	    	       

        self.assertIsNone(self.deck2[0])  	    	       
        self.assertIsNotNone(self.deck2[1])  	    	       
        self.assertIsNotNone(self.deck2[2])  	    	       
        self.assertIsNone(self.deck2[3])  	    	       

        self.assertIsNone(self.deck16[0])  	    	       
        self.assertIsNotNone(self.deck16[8]) 	    	       
        self.assertIsNotNone(self.deck16[16]) 	    	       
        self.assertIsNone(self.deck16[17]) 	    	       

        self.assertIsNone(self.deck8192[0]) 	    	       
        self.assertIsNotNone(self.deck8192[4096])	    	       
        self.assertIsNotNone(self.deck8192[8192])  	    	       
        self.assertIsNone(self.deck8192[8193]) 	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
