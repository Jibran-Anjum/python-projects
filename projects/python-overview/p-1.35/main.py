"""
The birthday paradox says that the probability
of two people in a room will have the same
birthday is more than half, provided n, the
number of people in the room, is more than 23.
This property is not really a paradox, but many
people find it surprising. Design a Python
program that can test this paradox by a series
of experiments on randomly generated birthdays,
which test this paradox for n = 5, 10, 15, 20,..., 100.
"""

def calc_probability(n):
    """Function to calculate the probability."""
    probability = 1.0
    for i in range(n):
        probability *= (365 - i)/365    # calculating probability

    probability -= 1

    return probability

if __name__ == '__main__':
    n = [i for i in range(5, 101, 5)]

    probability = 0

    for i in n:
        probability = calc_probability(i)
        print(f'Group size: {i}, Probability of shared birthdays: {-1*probability}')


