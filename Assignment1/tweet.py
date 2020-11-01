import math


MAX_TWEET_LENGTH = 50


HASHTAG_SYMBOL = '#'


MENTION_SYMBOL = '@'


UNDERSCORE = '_'


SPACE = ' '




def is_valid_tweet(text: str) -> bool:
    
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """

    return bool(1 <= len(text) <= MAX_TWEET_LENGTH)

        
    
def compare_tweet_lengths(text_1: str, text_2: str) -> int:
    
    """Return 1 if text_1 is longer than text_2, -1 if text_2 is longer 
    than text_1, and 0 if text_1 and text_2 have the same length.
    
    Precondition: 1<=len(text_1)<=MAX_TWEET_LENGTH and 
    1<=len(text_2)<=MAX_TWEET_LENGTH.
    
    >>> compare_tweet_lengths('Apple','Banana')
    -1
    >>> compare_tweet_lengths('Mango','Apple')
    0
    >>> compare_tweet_lengths('cscA08 is fun','No it is not')
    1
    
    """
    
    if len(text_1) > len(text_2):
        return 1
    elif len(text_1) < len(text_2):
        return -1
    else:
        return 0
    
    

###HELPER FUNCTION   
def potential_tweet_1(text_1: str, word_1: str, symbol: str) -> str:
    
    """Return the potential tweet if it is a valid tweet, else return text_1.
    Appending a space, symbol, and word_1 to the end of text_1
    results in a potential tweet.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word.
    
    >>> potential_tweet('I like HASHTAG_SYMBOLtravis','travis',HASHTAG_SYMBOL)
    'I like HASHTAG_SYMBOLtravisscott HASHTAG_SYMBOLtravisscott'
    >>> potential_tweet('MENTION_SYMBOLRed and','Blue',MENTION_SYMBOL)
    'MENTION_SYMBOLRed and MENTION_SYMBOLBlue'
    
    """
    
    potential_tweet = text_1 + SPACE + symbol + word_1
    if is_valid_tweet(potential_tweet):
        return potential_tweet
    else:
        return text_1


    
def add_hashtag(text_1: str, word_1: str) -> str:
    
    """Return the potential tweet if it is a valid tweet, else return text_1.
    Appending a space, a HASHTAG_SYMBOL, and word_1 to the end of text_1
    results in a potential tweet.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word.
    
    >>> add_hashtag('I like HASHTAG_SYMBOLcscA08','cscA08')
    'I like HASHTAG_SYMBOLcscA08 HASHTAG_SYMBOLcscA08'
    >>> add_hashtag('My favorite color is','Blue')
    'My favorite color is HASHTAG_SYMBOLBlue'
    
    """
    return potential_tweet_1(text_1, word_1, HASHTAG_SYMBOL)



###HELPER FUNCTION   
def contains_symbol(text_1: str, word_1: str, symbol: str) -> bool:
    
    """Return True if and only if text_1 contains a word made up from the
    symbol and word_1, else return False.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word.
    
    
    >>> contains_symbol('I like SYMBOLapplejuice!','applejuice',SYMBOL)
    True
    >>> contains_symbol('I like SYMBOLapplejuice','apple',SYMBOL)
    False
    
    """
    
    clean_tweet = clean(text_1) + SPACE 
    word_2 = word_1 + SPACE
    return bool(symbol + word_2 in clean_tweet)
    

    
def contains_hashtag(text_1: str, word_1: str) -> bool:
    
    """Return True if and only if text_1 contains a hashtag made up from the
    HASHTAG_SYMBOL and word_1, else return False.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word.
    
    >>> contains_hashtag('I like HASHTAG_SYMBOLspiderman','spiderman')
    True
    >>> contains_hashtag('I like HASHTAG_SYMBOLspiderman','spider')
    False
    
    """

    return contains_symbol(text_1, word_1, HASHTAG_SYMBOL)



def is_mentioned(text_1: str, word_1: str) -> bool:
    
    """Return True if and only if text_1 contains a hashtag made up from the
    MENTION_SYMBOL and word_1, else return False.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word.
    
    >>> is_mentioned('I like MENTION_SYMBOLpineappleonpizza','pineappleonpizza')
    True
    >>> is_mentioned('I like MENTION_SYMBOLpineappleonpizza','pineapple')
    False
    
    """
    
    return contains_symbol(text_1, word_1, MENTION_SYMBOL)



def add_mention_exclusive(text_1: str, word_1: str) -> str:
    
    """Return the potential tweet if it is a valid tweet AND word_1
    doesn't already appear in text_1 with MENTION_SYMBOL as the preceding
    character, else return text_1.
    
    Appending a space, a MENTION_SYMBOL, and word_1 to the end of text_1
    results in a potential tweet.
    
    Preconditions: 1<=len(text_1)<=MAX_TWEET_LENGTH and word_1 is a valid 
    tweet word
    
    >>> add_hashtag('I like MENTION_SYMBOLmintchocochipicecream','icecream')
    'I like MENTION_SYMBOLmintchocochipicecream MENTION_SYMBOLicecream'
    >>> add_hashtag('My favorite color is MENTION_SYMBOLBlue','Blue')
    'My favorite color is MENTION_SYMBOLBlue'
    
    """
    clean_tweet = clean(text_1) + SPACE
    word_2 = word_1 + SPACE
    if MENTION_SYMBOL + word_2 in clean_tweet:
        return text_1
    else:
        return potential_tweet_1(text_1, word_1, MENTION_SYMBOL)



def num_tweets_required(message: str) -> int:
    
    """Return the minimum number of tweets required to communicate message.
    
    >>> num_tweets_required('abcd')
    1
    >>> num_tweets_required(1000 * 'abcdefghij')
    200
    """
    
    num_tweet = len(message)/MAX_TWEET_LENGTH
    return math.ceil(num_tweet)
    


def get_nth_tweet(message: str, n: int) -> str:
    
    """Return the nth tweet when message is split into valid tweets of length
    MAX_TWEET_LENGTH when the nth tweet exists, else return an empty string
    Precondition: n >= 0.
    
    >>> get_nth_tweet(2 * 'abcdefghijklmnopqrstuvwxyz',1)
    'yz'
    >>>get_nth_tweet('aiebd;iwed',1)
    ''
    
    """
        
    return message[n * MAX_TWEET_LENGTH:((n+1) * MAX_TWEET_LENGTH)]


def clean(text: str) -> str:
    
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
