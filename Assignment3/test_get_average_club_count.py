"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_check_modification(self):
        """ Test get_average_club_count to check that it does not modify the
        input.
        
        """
        
        param = {'A':[1, 2, 3, 4], 'B':[1, 2, 3], 'C':[1]}
        param_duplicate = param.copy()
        return_value = club_functions.get_average_club_count(param)
        actual = bool(param == param_duplicate)
        expected = True
        msg = "Function modifies the input".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
    
    def test_00_empty(self):
        """ Test get_average_club_count with an empty dictionary.
        
        """        
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        """ Test get_average_club_count with a single key single value
        dictionary.
        
        """         
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_02_one_person_five_clubs(self):
        """ Test get_average_club_count with a single key multiple value
        dictionary.
        
        """         
        param = {'Luke Dunphy': ['A', 'B', 'C', 'D', 'E']}
        actual = club_functions.get_average_club_count(param)
        expected = 5.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg) 
        
    def test_03_five_people_one_club_each(self):
        """ Test get_average_club_count with a multiple key single value each
        dictionary.
        
        """         
        param = {'Michelle Tanner': ['Comet Club'],
                 'Danny R Tanner': ['Parent Council'],
                 'Kimmy Gibbler': ['Rock N Rollers'],
                 'Jesse Katsopolis': ['Parent Council'],
                 'Joey Gladstone': ['Comics R Us']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_04_three_people_varying_clubs(self):
        """ Test get_average_club_count with a multiple key variable values
        (either single or multiple) dictionary.
        
        """         
        param = {'Michelle Tanner': ['Comet Club'],
                 'Danny R Tanner': ['Parent Council'],
                 'Kimmy Gibbler': ['Rock N Rollers', 'Parent Council', 'C']}
        actual = club_functions.get_average_club_count(param)
        expected = 5/3
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)    
        
    def test_05_five_people_five_club_each(self):
        """ Test get_average_club_count with a multiple key multiple values
        dictionary.
        
        """         
        param = {'Manny Delgado': ['A', 'B', 'C', 'D', 'E'],
                 'Mitchell Pritchett': ['F', 'G', 'H', 'I', 'J'],
                 'Alex Dunphy': ['K', 'L', 'M', 'N', 'O'],
                 'Cameron Tucker': ['P', 'Q', 'R', 'S', 'T'],
                 'Phil Dunphy': ['U', 'V', 'W', 'X', 'Y']}
        actual = club_functions.get_average_club_count(param)
        expected = 5.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)    
if __name__ == '__main__':
    unittest.main(exit=False)
