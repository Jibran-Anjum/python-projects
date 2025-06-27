"""
Write a Python program that takes a positive integer greater than 2
as input and write out the number of times that repeatedly divide
this number by 2 before getting a value less than 2.
"""

def div_by_2(val):
    
    count = 0

    while True:
        if val < 2:
            break
        val /= 2
        count += 1
    
    return count


if __name__ == '__main__':
    val = int(input("Value: "))

    if val < 2:
        print(f'Value is already less than 2. ({val} < 2)')
        quit()
    div_no_of_times = div_by_2(val)
    print(f'The no. of times {val} needed to by divided by 2 to get a value\nthat is less than 2 is\n-> {div_no_of_times}.')