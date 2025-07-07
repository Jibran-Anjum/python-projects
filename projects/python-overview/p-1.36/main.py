"""
Write a Python program that inputs a list of words,
seperated by whitespace, and output how many times
each word appears in the list. You need to not
worry about efficiency at this point.
"""

def list_input():
    """Take input from the user.
    
    Then split the input by the ' ' whitespace
    converting the user input into a list of
    words.
    """

    lst = input('>> ')         # Taking user input
    the_lst = lst.split(' ')   # converting the user input into a list of words
    return the_lst

def count(lst):
    """Count how many times each element is
    repeated inside the list of words."""

    count = {}
    for i in lst:
        count.setdefault(i, 0)

    """Check whether there is word is in the list."""
    for i in lst:
        for j in lst:
            if i is j:
                count[i] += 1    #   Then add 1 to the count that is 0 by default

    return count

if __name__ == '__main__':
    lst = list_input()     # function call
    output = count(lst)    # function call
    print(output)          # print output
    
