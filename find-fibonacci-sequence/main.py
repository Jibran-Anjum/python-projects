user_input = int(input('Enter a value: '))

elem1 = elem2 = 1
sum = 0

print(elem1)

for i in range(1, user_input):
    if i == 1:
        print(elem1)
        continue
    else:
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
        print(sum)
