''' Week 4 worksheet: starter code. '''


def count_uppercase(text: str) -> int:
    """Return the number of uppercase letters in text.

    >>> count_uppercase('hjbhbAKBKBbjBbkjBjbdB')
    8
    >>> count_uppercase('#@%&^$64865B')
    1

    """
    
    counter = 0
    for ch in text:
        if ch.isupper():
            counter = counter + 1
    return counter


def all_fluffy(text: str) -> bool:
    """Return True iff every character in text is fluffy. Fluffy
    characters are those that appear in the word 'fluffy'. Return True
    is text is empty.

    >>> all_fluffy('aojebfpiaf')
    False
    >>> all_fluffy('flufyulfyulyfu')
    True
    
    """

    for ch in text:
        if ch not in 'fluy':
            return False
    return True
            


def add_underscores(text: str) -> str:
    """Return a string that contains the characters from text with an
    underscore added after every character except the last.

    >>>"apple"
    'a_p_p_l_e'
    >>>'1243jn'
    '1_2_4_3_j_n'
    
    """

    string = ''
    for ch in text:
        string = string + ch + '_'
    return string[:-1]
