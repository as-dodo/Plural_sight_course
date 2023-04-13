# Get details of loan
money_owed = float(input('How much money do you owe in dollars?\n'))  # 50,000
apr = float(input('What is an annual percentage rate of the loan?\n'))  # 3
payment = float(input('How much will you pay off each month in dollars?\n'))  # 1,000
months = int(input('How many months do you want to see the results for?\n'))  # 54

monthly_rate = apr / 100 / 12

for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add an interest
    money_owed += interest_paid
    if (money_owed - payment) < 0:
        print(f'The last payment is {round(money_owed, 2)}')
        print(f'You paid off the loan in {i+1} months')
        break
    # Make payment
    money_owed -= payment


    print(f'Paid {payment} of which {interest_paid} was interest.', end=' ')
    print(f'Now I owe {money_owed}')


