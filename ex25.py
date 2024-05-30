def break_words(stuff):             #Function to split the string inside the variable "stuff" and returned the output
    """This is fuction will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):         #Function to sort the string
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):        #Function to remove and print first word 
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):         #Function to remove and print last word 
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):        #Function to sort the splitted word
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):     #Function to print and remove first and last word
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence): #Function to print and remove last and first sorted word
    """Sorts the word then prints first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
