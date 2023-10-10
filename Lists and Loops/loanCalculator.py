#Get Details of Loan

#Example Value: $50,000
money_owed = float(input('How much money do you own, in dollars? \n')) 
#Annual Percentage Rate (example 3%)
apr = float(input('What is the annual percentage rate of the loan? \n'))
#Example Value $ 1,000
payment = float(input('How much will you pay off each month? \n')) 
#Example Value 24 Months
months = int(input('How many months do you want to see the results for? \n'))

monthly_rate = apr/100/12

for i in range(months):
    #Calculate Interest to Pay
    interest_paid = round(money_owed * monthly_rate)

    #Add in Interest
    money_owed = round(money_owed + interest_paid)

    if (money_owed - payment < 0):
        print(f'The last payment is {money_owed}. You paid off the loan in {i+1} months.')
        break
    # Make Payment
    money_owed = money_owed - payment

    print(f"You've paid ${payment} of which ${interest_paid} was interest")
    print(f'Now I owe ${money_owed}')