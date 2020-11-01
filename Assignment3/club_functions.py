"""Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO

# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)
        
        
        

def friends_and_clubs(profile: List[str]) -> List[List[str]]:
    """ Return a list consisted of two unsorted nested lists friends and clubs
    respectively, from profile.
    
    >>> test_case_0 = ['Pritchett, Jay', 'Pritchett, Gloria', 'Delgado, Manny',
    ...    'Dunphy, Claire']
    >>> friends_and_clubs(test_case_0)
    [['Gloria Pritchett', 'Manny Delgado', 'Claire Dunphy'], []]
    >>> test_case_1 = ['Tucker, Cameron', 'Clown School',
    ...    'Wizard of Oz Fan Club', 'Pritchett, Mitchell']
    >>> friends_and_clubs(test_case_1)
    [['Mitchell Pritchett'], ['Clown School', 'Wizard of Oz Fan Club']]
    """
    
    friends, clubs = [], []
    if len(profile[1:]) != 0:
        profile[0] = format_changer(profile[0])
        for connection in profile[1:]:
            if ", " in connection:
                connection = format_changer(connection)
                friends.append(connection)
            else:
                clubs.append(connection)
    return [friends, clubs]




def format_changer(person: str) -> str:
    """ Return the name of person in profiles.txt in FirstName (s) LastName
    format.
    
    Precondition: ', ' in person == True.
    
    >>> format_changer('Pritchett, Ya-boyy')
    'Ya-boyy Pritchett'
    >>> format_changer('Dunphy, Haley Gwendolyn\\n')
    'Haley Gwendolyn Dunphy'
    
    """    
    
    name_list = person.split(', ')
    return name_list[1].strip('\n') + ' ' + name_list[0]




def recommend_clubs_friends(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> Dict[str, int]:
    """Return a dictionary that maps the clubs that friends of person from
    "person to friends" dictionary person_to_friends are a part of but person
    is not using the "person to clubs" dictionary person_to_clubs, to the
    number of friends that are in that club.
    
    >>> recommend_clubs_friends(P2F, P2C, 'Stephanie J Tanner')
    {'Comet Club': 1, 'Rock N Rollers': 1, 'Smash Club': 1}
    >>> recommend_clubs_friends(P2F, P2C, 'Jesse Katsopolis')
    {'Comics R Us': 1}
    
    """
    
    club_score = {}
    clubs_of_friends = (get_clubs_of_friends
                        (person_to_friends, person_to_clubs, person))
    for club in clubs_of_friends:
        if club not in club_score:
            club_score[club] = clubs_of_friends.count(club)
    return club_score




def recommend_clubs_acquaintance(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> Dict[str, List[str]]:
    """Return a dictionary that maps the potential clubs that person might
    wish to join, to their potential score based on "person to clubs" dictionary
    person_clubs and "person to friends" dictionary person_to_friends.
    
    Precondition: person in person_to_clubs == True.
    
    >>> recommend_clubs_acquaintance(P2F, P2C, 'Danny R Tanner')
    {'Comics R Us': 2, 'Rock N Rollers': 2}
    >>> recommend_clubs_acquaintance(P2F, P2C, 'Jesse Katsopolis')
    {'Comics R Us': 2, 'Smash Club': 1}
    
    """
    
    club_to_people = invert_and_sort(person_to_clubs)
    club_score = (recommend_clubs_friends
                  (person_to_friends, person_to_clubs, person))
    lst = []
    for club in person_to_clubs[person]:
        for friend in club_to_people[club]:
            for new_club in person_to_clubs[friend]:
                lst.append(new_club)
    for club in person_to_clubs[person]:
        while club in lst:
            lst.remove(club)
    for club in lst:
        if club not in club_score:
            club_score[club] = 1
        else:
            club_score[club] = club_score[club] + 1
    return club_score




def recommend_club_sorter(club_recommendation: List[Tuple[str, int]]) -> None:
    """ Modify the list of two pair tuples in club_recommendation in descending
    order based on the second element of each tuple, and in alphabetical order
    if the values of the second element in the tuple are the same.
    
    >>> test_list_0 = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
    >>> recommend_club_sorter(test_list_0)
    >>> test_list_0
    [('d', 4), ('c', 3), ('b', 2), ('a', 1)]
    >>> test_list_1 = [('a', 5), ('A', 5), ('B', 6), ('c', 5)]
    >>> recommend_club_sorter(test_list_1)
    >>> test_list_1
    [('B', 6), ('A', 5), ('a', 5), ('c', 5)]
    
    """
    
    club_recommendation.sort()
    len_list = len(club_recommendation)
    for i in range(len_list):
        for j in range(len_list - i - 1):
            if club_recommendation[j][1] < club_recommendation[j + 1][1]:
                temp = club_recommendation[j]
                club_recommendation[j] = club_recommendation[j + 1]
                club_recommendation[j + 1] = temp


# Required functions
def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file.

    NOTE: Functions (including helper functions) that have a parameter
          of type TextIO do not need docstring examples.

    """
    
    person_to_friends, person_to_clubs, profiles = {}, {}, []
    lst = profiles_file.read().splitlines()
    if lst == []:
        return ({}, {})
    lst.append('')
    while '' in lst:
        profiles.append(lst[0:lst.index('')])
        lst = lst[lst.index('') + 1:]
    for profile in profiles:
        person = format_changer(profile[0])
        connections = friends_and_clubs(profile)
        friends, clubs = connections[0], connections[1]
        for friend in friends:
            update_dict(person, friend, person_to_friends)
        for club in clubs:
            update_dict(person, club, person_to_clubs)
    for person in person_to_friends:
        person_to_friends[person].sort()
    for person in person_to_clubs:
        person_to_clubs[person].sort()
    return (person_to_friends, person_to_clubs)    
            
                


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    >>> test_case = {'A':[1, 2, 3, 4], 'B':[1, 2, 3], 'C':[1]}
    >>> get_average_club_count(test_case) == 8/3
    True
    
    """
    
    if len(person_to_clubs) == 0:
        return 0.0
    total = 0
    for person in person_to_clubs:
        total = total + len(person_to_clubs[person])
    return total/len(person_to_clubs)

def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people
    from the "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    >>> test_case = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett',
    ...    'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett',
    ...    'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado':
    ...    ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
    ...    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy',
    ...    'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':
    ...    ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy':
    ...    ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy',
    ...    'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat',
    ...    'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker',
    ...    'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy',
    ...    'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_last_to_first(test_case) == {'Pritchett': ['Gloria', 'Jay',
    ...    'Mitchell'], 'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn', 'Luke',
    ...    'Phil'], 'Delgado': ['Manny'], 'Tucker': ['Cameron'], 'D-Money':
    ...    ['Dylan'], 'D-Cat': ['Chairman', 'Gilbert']}
    True
    """
    last_to_first = {}
    for person in person_to_friends:
        name_person = person.rsplit(' ', 1)
        update_dict(name_person[1], name_person[0], last_to_first)
        for friend in person_to_friends[person]:
            name_friend = friend.rsplit(' ', 1)
            update_dict(name_friend[1], name_friend[0], last_to_first)
    for person in last_to_first:
        last_to_first[person].sort()
    return last_to_first
        
            


def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    >>> test_case = {'A': 1, 'B': (1, 2, 'hello'), 'C': 'hello'}
    >>> invert_and_sort(test_case)
    {1: ['A'], (1, 2, 'hello'): ['B'], 'hello': ['C']}

    """
    inverted = {}
    for key in key_to_value:
        if type(key_to_value[key]) == list:
            for value in key_to_value[key]:
                update_dict(value, key, inverted)
            for value in inverted:
                inverted[value].sort()
        else:
            update_dict(key_to_value[key], key, inverted)
        
    return inverted


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    >>> get_clubs_of_friends(P2F, P2C, 'Jesse Katsopolis')
    ['Comics R Us']
    
    """
    
    clubs_of_friends = []
    if person not in person_to_friends:
        return []
    for friend in person_to_friends[person]:
        if friend in person_to_clubs:
            for club in person_to_clubs[friend]:
                clubs_of_friends.append(club)
    if person in person_to_clubs:
        for club in person_to_clubs[person]:
            while club in clubs_of_friends:
                clubs_of_friends.remove(club)
    clubs_of_friends.sort()
    return clubs_of_friends


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    >>> recommend_clubs(P2F, P2C, 'Danny R Tanner',)
    [('Comics R Us', 2), ('Rock N Rollers', 2)]
    
    """
    
    club_recommendation = []
    club_score = (recommend_clubs_friends
                  (person_to_friends, person_to_clubs, person))
    if person in person_to_clubs:
        club_score = (recommend_clubs_acquaintance
                      (person_to_friends, person_to_clubs, person))
    for club in club_score:
        club_recommendation.append((club, club_score[club]))
    recommend_club_sorter(club_recommendation)
    return club_recommendation


if __name__ == '__main__':
    pass
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    #import doctest
    #doctest.testmod()