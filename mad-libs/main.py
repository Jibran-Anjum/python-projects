try:
    fhand = open('story.txt')
except:
    print('File not found')
    quit()


print('The Story:\n')

print('alice woke up at 3am took a ____ ______ and then went back to sleep on a ______ night. but it was still too ___ so she couldn\'t sleep.\nshe kept on changing her ________ position over and over again and before she noticed it was 7am and the sun started to rise making the weather even hotter.\nshe screamed as she got out of ___, \'i didn\'t even get a wink of sleep.\'\n___ and sleepy she had to go to school on top of it. so she got ready and went to school in a really ___ mood.')

guess = list()

for i in range(8):
    print('Guess No.', i+1, ': ', end='')
    inp = input()
    guess.append(inp)

print('\n')
print('Your Story: ')
print('\n')
print('alice woke up at 3am took a', guess[0], guess[1], 'and then went back to sleep on a', guess[2], 'night. but it was still too', guess[3], 'so she couldn\'t sleep.\nShe kept on changing her', guess[4], 'position over and over again and before she noticed it was 7am and the sun started to rise making the weather even hotter.\nshe screamed as she got out of', guess[5], '\'i didn\'t even get a wink of sleep.\'\n', guess[6], 'and sleepy she had to go to school on top of it. so she got ready and went to school in a really', guess[7], 'mood.')

print('\n')
print('The Real Story: ')
print('\n')
for line in fhand:
    line = line.rstrip()
    print(line)
