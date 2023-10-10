total = 0
expenses = []
num_expenses = int(input("Enter # of Expense:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an Expense:")))

total = sum(expenses)

print(f'You total money spent is ${total}.')