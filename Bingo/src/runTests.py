import unittest
from Testing import testMenu, testMenuOption, testRandNumberSet, testCard, testDeck  	    	       

suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testMenu.TestMenu))  	    	       
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testMenuOption.TestMenuOption))  	    	       
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testRandNumberSet.TestRandNumberSet))  	    	       
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCard.TestCard))  	    	       
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testDeck.TestDeck))  	    	       

unittest.TextTestRunner(verbosity=2).run(suite)  	    	       
