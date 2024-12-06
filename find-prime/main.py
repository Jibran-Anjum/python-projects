usr_input = int(input('Enter a limit of the prime numbers: '))

is_prime = True

for i in range(2, usr_input + 1):
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        print(i)
    else:
        continue
    
