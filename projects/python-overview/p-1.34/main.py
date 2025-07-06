"""
A common punishment for school children is
to write out a sentence multiple times.
Write a Python stand-alone program that will
write out the following sentence one hundred
times: 'I will never spam my friends again.'
Your program should number each of the sentences
and it should make eight different random-looking
typos.
"""

def write():
    """Print out the sentence 100 times.

    With eight random typos.
    """
    sentence = 'I will never spam my friends again.'
    for i in range(1, 101):
        """Random typos"""
        if i == 25:
            print(f'{i}. I will nevr spam my friends again.')
            continue
        if i == 40:
            print(f'{i}. I wll never spam my friends again.')
            continue
        if i == 43:
            print(f'{i}. I will never spm my friends again.')
            continue
        if i == 48:
            print(f'{i}. I will never spam my freinds again.')
            continue
        if i == 58:
            print(f'{i}. I will never spam my friends agian.')
            continue
        if i == 62:
            print(f'{i}. I will never spam my friedns again.')
            continue
        if i == 67:
            print(f'{i}. I will never spma my friends again.')
            continue
        if i == 97:
            print(f'{i}. I will nevre spam my friends again.')

        """The sentence."""
        print(f'{i}. {sentence}')



if __name__ == '__main__':
    write()    # Function call
