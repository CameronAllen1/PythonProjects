import unittest  	    	       

from MenuOption import MenuOption  	    	       


class TestMenuOption(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """Create no fewer than 5 MenuOption objects to test"""  	    	       
        self.a = MenuOption("A", "Test option A")  	    	       
        self.b = MenuOption("B", "Test option B")  	    	       
        self.c = MenuOption("C", "Test option C")  	    	       
        self.d = MenuOption("D", "Test option D")  	    	       
        self.e = MenuOption("E", "Test option E")  	    	       

    def test_chCommand(self):  	    	       
        """Ensure each option's letter char is set correctly"""  	    	       
        self.assertEqual(self.a.chCommand(), "A")  	    	       
        self.assertEqual(self.b.chCommand(), "B")  	    	       
        self.assertEqual(self.c.chCommand(), "C")  	    	       
        self.assertEqual(self.d.chCommand(), "D")  	    	       
        self.assertEqual(self.e.chCommand(), "E")  	    	       

    def test_szDescription(self):  	    	       
        """Ensure each option's description is set correctly"""  	    	       
        self.assertEqual(self.a.szDescription(), "Test option A")  	    	       
        self.assertEqual(self.b.szDescription(), "Test option B")  	    	       
        self.assertEqual(self.c.szDescription(), "Test option C")  	    	       
        self.assertEqual(self.d.szDescription(), "Test option D")  	    	       
        self.assertEqual(self.e.szDescription(), "Test option E")  	    	       

    def test_str(self):  	    	       
        """Ensure the __str__ dunder works correctly"""  	    	       
        self.assertEqual(str(self.a), "A) Test option A")  	    	       
        self.assertEqual(str(self.b), "B) Test option B")  	    	       
        self.assertEqual(str(self.c), "C) Test option C")  	    	       
        self.assertEqual(str(self.d), "D) Test option D")  	    	       
        self.assertEqual(str(self.e), "E) Test option E")  	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
