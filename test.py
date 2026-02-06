"""
Testing library
""" 
import unittest
from unittest.mock import patch
from io import StringIO
#import our user made function for testing
from personal_library import(
    add_book,
    remove_book,
    list_book,
    search_book
)
#test class 
class TestPersonallibrary(unittest.TestCase):
    #test case for add book function
    def test_add_book_normal_case(self):
        library =[]
        with patch("builtins.input",return_value ="Dune"):
           add_book(library)
        
        self.assertEqual(library, ["Dune"])

    #test case for duplicates in add book function (needs fixing)
    def test_add_book_duplicate_case(self):
        library =[]
        with patch("builtins.input",return_value ="Dune"):
           add_book(library)
           add_book(library)
        
        self.assertEqual(library, ["Dune"])

    #test case of list book function
    def test_list_more_than_one_book(self):
        library= ["Dune","Dune Messiah"]
        with patch("sys.stdout",new=StringIO()) as out:
            list_book(library)
            output = out.getvalue()
        self.assertIn("Dune", output)
        self.assertIn("Dune Messiah", output)
      

    

#call the test class main method

if __name__ == "__main__":
    unittest.main()