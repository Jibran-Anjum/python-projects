def fibonacci_seq(n):
    """Print out upto n (length) fibonacci sequence."""
    elem1 = 0
    elem2 = 1

    if n == 1:
        print(elem1)
        quit()

    if n > 1:
        print(elem1)
        print(elem2)

    for i in range(n-2):
        sum = elem1 + elem2
        print(sum)
        elem1, elem2 = elem2, sum

n = int(input('Element number: '))
fibonacci_seq(n)
