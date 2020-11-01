"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_check_modification(self):
        """ Test get_last_to_first to check that it does not modify the input.
        
        """
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett',
                                   'Manny Delgado'],
                 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett',
                                   'Phil Dunphy'],
                 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett',
                                   'Luke Dunphy'],
                 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy',
                                  'Luke Dunphy'],
                 'Alex Dunphy': ['Luke Dunphy'],
                 'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],
                 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
                 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],
                 'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
                 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett',
                                      'Manny Delgado'],
                 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado',
                                 'Mitchell Pritchett', 'Phil Dunphy']}
        param_duplicate = param.copy()
        return_value = club_functions.get_last_to_first(param)
        actual = bool(param == param_duplicate)
        expected = True
        msg = "Function modifies the input".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_00_empty(self):
        """ Test get_last_to_first with an empty dictionary.
        
        """        
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        """ Test get_last_to_first with a single key single value (same
        last name) dictionary.
        
        """         
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_02_one_person_one_friend_different_last(self):
        """ Test get_last_to_first with a single key single value (different
        last name) dictionary.
        
        """                 
        param = {'Clare Dunphy': ['Jay Pritchett']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'],
                    'Pritchett': ['Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_03_one_person_four_friends_same_last(self):
        """ Test get_last_to_first with a single key multiple value (all same
        last name) dictionary.
        
        """        
        param = {'Clare Dunphy': (['Phil Dunphy', 'Haley Gwendolyn Dunphy',
                                   'Luke Dunphy', 'Alex Dunphy'])}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': (['Alex', 'Clare', 'Haley Gwendolyn',
                                'Luke', 'Phil'])}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_04_one_person_four_friend_mixed(self):
        """ Test get_last_to_first with a single key multiple value (some with
        the same last name) dictionary.
        
        """         
        param = {'Clare Dunphy': (['Jay Pritchett', 'Manny Delgado', 
                                   'Luke Dunphy', 'Dylan D-money'])}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Luke'],
                    'Pritchett': ['Jay'],
                    'Delgado': ['Manny'],
                    'D-money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_05_one_person_four_friend_different_last(self):
        """ Test get_last_to_first with a single key multiple value (all with
        different last names) dictionary.
        
        """        
        param = {'Clare Dunphy': (['Jay Pritchett', 'Manny Delgado', 
                                   'Scrooge McDuck', 'Dylan D-money'])}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'],
                    'Pritchett': ['Jay'],
                    'Delgado': ['Manny'],
                    'McDuck': ['Scrooge'],
                    'D-money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
    def test_06_four_people_one_friend_each_same_last(self):
        """ Test get_last_to_first with multiple key single value (same last
        name as its key) dictionary.
        
        """         
        param = {'Clare Dunphy': ['Haley Gwendolyn Dunphy'],
                 'Haley Gwendolyn Dunphy': ['Alex Dunphy'], 
                 'Jay Pritchett': ['Gloria Pritchett'],
                 'Manny Delgado': ['Javier Hectoro Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Alex', 'Clare', 'Haley Gwendolyn'],
                    'Pritchett': ['Gloria', 'Jay'],
                    'Delgado': ['Javier Hectoro', 'Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_07_four_people_one_friend_each_mixed(self):
        """ Test get_last_to_first with multiple key single value (some with
        same last name as its key) dictionary.
        
        """         
        param = {'Clare Dunphy': ['Haley Gwendolyn Dunphy'],
                 'Haley Gwendolyn Dunphy': ['Dylan D-Money'], 
                 'Jay Pritchett': ['Gloria Pritchett'],
                 'Manny Delgado': ['Luke Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Haley Gwendolyn', 'Luke'],
                    'Pritchett': ['Gloria', 'Jay'],
                    'Delgado': ['Manny'],
                    'D-Money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_08_four_people_one_friend_each_different_last(self):
        """ Test get_last_to_first with multiple key single value (all with
        different last name than its key) dictionary.
        
        """        
        param = {'Clare Dunphy': ['Jay Pritchett'],
                 'Manny Delgado': ['Scrooge McDuck'],
                 'Haley Gwendolyn Dunphy': ['Dylan D-money'], 
                 'Jay Pritchett': ['Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Haley Gwendolyn'],
                    'Pritchett': ['Jay'],
                    'Delgado': ['Manny'],
                    'McDuck': ['Scrooge'],
                    'D-money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_09_four_people_four_friends_each_same_last(self):
        """ Test get_last_to_first with multiple key multiple value (all same
        last name as their respective keys) dictionary.
        
        """        
        param = {'a A': ['b A', 'c A', 'd A', 'e A'],
                 'b B': ['a B', 'c B', 'd B', 'e B'],
                 'z A': ['a A', 'y A', 't A', 'q A'],
                 'm M': ['e M', 'j M', 'o M', 't M'],}
        actual = club_functions.get_last_to_first(param)
        expected = {'A': ['a', 'b', 'c', 'd', 'e', 'q', 't', 'y', 'z'],
                    'B': ['a', 'b', 'c', 'd', 'e'],
                    'M': ['e', 'j', 'm', 'o','t']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_10_four_people_four_friends_each_mixed(self):
        """ Test get_last_to_first with multiple key multiple value (some with
        same last name as their respective keys) dictionary.
        
        """         
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett',
                                   'Manny Delgado', 'Cameron Tucker'],
                 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett',
                                   'Phil Dunphy', 'Dylan D-Money'],
                 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett',
                                   'Luke Dunphy','Javier Hectoro Delgado'],
                 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy',
                                        'Luke Dunphy', 'Jay Pritchett']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell'],
                    'Dunphy': ['Claire', 'Luke', 'Phil'],
                    'Delgado': ['Javier Hectoro', 'Manny'],
                    'Tucker': ['Cameron'], 'D-Money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_11_four_people_four_friends_each_different_last(self):
        """ Test get_last_to_first with multiple key multiple value (all with
        different last names than their respective keys) dictionary.
        
        """         
        param = {'a A': ['b B', 'c C', 'd D', 'e E'],
                 'b B': ['a A', 'c C', 'd D', 'e E'],
                 'z Z': ['a B', 'c D', 'e F', 'g H'],
                 'm M': ['e F', 'g H', 'i J', 'a A'],}
        actual = club_functions.get_last_to_first(param)
        expected = {'A': ['a'],
                    'B': ['a', 'b'],
                    'C': ['c'],
                    'D': ['c', 'd'],
                    'E': ['e'],
                    'F': ['e'],
                    'H': ['g'],
                    'Z': ['z'],
                    'M': ['m'],
                    'J': ['i']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
if __name__ == '__main__':
    unittest.main(exit=False)