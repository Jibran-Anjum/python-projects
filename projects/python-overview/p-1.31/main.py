"""
Write a Python program that can "make change".
Your program should take two numbers as input,
one that is monetary amount charged and the
other is monetary amount given. It should then
return the number of each kind of bill and coin
to give back as change for the difference
between the amount given and the amount charged.
The values assigned to the bills and coins can
be based on the monetary system of any current
or former government. Try to design your program
so that it returns as few bills and coins as
possible.
"""

def calc_change(amount_charged, amount_given):
    """Calculates the change.

    First we create bills and coins list that
    holds the bills and coins.
    """
    bills = [100, 50, 20, 10, 1]
    coins =  [0.25, 0.10, 0.05, 0.01]

    return_bill = []    # empty list (it'll store the return bills and coins)

    """If amount charged is less than amount given
    then return amount is amount given minus the
    amount charged
    """
    if amount_charged < amount_given:
        return_amount = amount_given - amount_charged
    else:    # If not then the function ends here
        print('Amoung given is less than the amount charged.')
        return

    return_amount = round(return_amount, 2)    # round the return amount to 2 decimal points

    print('Return amount:', return_amount)

    """
    Calculating the bills to be returned.
    """
    while int(return_amount) != 0:
        """
        Sequence of conditional statements for the
        bills. if they satisfy the condition, it is
        appended to the return_bill list, and the
        value is subtracted from the return amount.
        """
        if int(return_amount) >= bills[0]:
            return_bill.append(bills[0])
            return_amount -= bills[0]
        elif int(return_amount) >= bills[1] and int(return_amount) < bills[0]:
            return_bill.append(bills[1])
            return_amount -= bills[1]
        elif int(return_amount) >= bills[2] and int(return_amount) < bills[1]:
            return_bill.append(bills[2])
            return_amount -= bills[2]
        elif int(return_amount) >= bills[3] and int(return_amount) < bills[2]:
            return_bill.append(bills[3])
            return_amount -= bills[3]
        elif int(return_amount) >= bills[4] and int(return_amount) < bills[3]:
            return_bill.append(bills[4])
            return_amount -= bills[4]

    """
    Calculating the coins to return.
    """
    while return_amount != 0:
        """
        Sequence of conditional statements for the
        coins. if they satisfy the condition, it is
        appended to the return_bill list, and the
        value is subtracted from the return amount.
        """
        return_amount = round(return_amount, 2)
        if return_amount < bills[4] and return_amount >= coins[0]:
            return_bill.append(coins[0])
            return_amount -= coins[0]
        elif return_amount < coins[0] and return_amount >= coins[1]:
            return_bill.append(coins[1])
            return_amount -= coins[1]
        elif return_amount < coins[1] and return_amount >= coins[2]:
            return_bill.append(coins[2])
            return_amount -= coins[2]
        elif return_amount < coins[2] and return_amount >= coins[3]:
            return_bill.append(coins[3])
            return_amount -= coins[3]

    return return_bill    # the list return_bill is returned

if __name__ == '__main__':
    """
    Taking input from the user and storing in
    variables.
    """
    amount_charged = float(input('Amount charged: '))
    amount_given = float(input('Amount given: '))

    bills = calc_change(amount_charged, amount_given)    # call to the function and storing the return value
    if bills is None:    # if return value is None quit
        quit()

    one = 0    # holds the number of ones
    ten = 0    # holds the number of tens
    twenty = 0    # holds the number of twenties
    fifty = 0    # holds the number of fifties
    hundred = 0    # holds the number of hundreds
    quarter= 0    # holds the number of quarters
    dime = 0    # holds the number of dimes
    nickle = 0    # holds the number of nickles
    penny = 0    # holds the number of pennies

    for i in range(len(bills)):
        """Loop to count the number of bills or coins."""

        if bills[i] == 100:
            hundred += 1
            continue
        if bills[i] == 50:
           fifty += 1
           continue
        if bills[i] == 20:
           twenty += 1
           continue
        if bills[i] == 10:
           ten += 1
           continue
        if bills[i] == 1:
           one += 1
           continue
        if bills[i] == 0.25:
           quarter += 1
           continue
        if bills[i] == 0.10:
           dime += 1
           continue
        if bills[i] == 0.05:
           nickle += 1
           continue
        if bills[i] == 0.01:
           penny += 1
           continue
    
    """Printing out the bills one by one."""
    if one > 0:
        print(one, 'x 1 bill')
    if ten > 0:
        print(ten, 'x 10 bill')
    if twenty > 0:
        print(twenty, 'x 20 bill')
    if fifty > 0:
        print(fifty, 'x 50 bill')
    if hundred > 0:
        print(hundred, 'x 100 bill')
    if quarter > 0:
        print(quarter, 'x 0.25 coins')
    if dime > 0:
        print(dime, 'x 0.10 coins')
    if nickle > 0:
        print(nickle, 'x 0.05 coins')
    if penny > 0:
        print(penny, 'x 0.01 coins')

