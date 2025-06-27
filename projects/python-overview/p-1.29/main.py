"""
Write a program that outputs all possible strings by
using the characters 'c', 'a', 't', 'd', 'o', and 'g'
exactly once.
"""

def permutations(chars):
    """Finds the permutations and append it into
    the list named permutes."""

    if len(chars) == 1:                   # checks if length is 1
        return chars[0]                   # return the 1 element

    permutes = []                         # empty list

    for i in range(len(chars)):
        char = chars[i]                   # Stores the iterated value via iterator
        rest = chars[:i] + chars[i+1:]    # Stores the rest of the values of the list
        for perm in permutations(rest):   # recursive call to permutation with rest as it's argument
            permutes.append(char + perm)  # append permutes with the character and the perm value

    return permutes

if __name__ == '__main__':
    chars = ['c', 'a', 't', 'd', 'o', 'g']
    perms = permutations(chars)

    print(perms)
