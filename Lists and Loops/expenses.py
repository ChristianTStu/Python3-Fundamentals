expenses = [10.50, 8, 5, 15, 20, 5, 3]

total_expenses = 0

for x in expenses:
    total_expenses = total_expenses + x

print(f'You spent ${total_expenses} dollars.')


# OR you can use the built in sum function within Python. 

lunch_cost = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(lunch_cost)

print(f'You spent ${total} dollars.')