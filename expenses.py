# expenses = [10.50, 8, 5, 15, 20, 5, 3]
#
# tot = 0
#
# for expense in expenses:
#     tot += expense
#
# print(f"You spent $ {tot}")
#
# total = sum(expenses)
# print(f"You spent $ {total}")

expenses = []
num_expenses = int(input('Enter # of expenses: '))

for i in range(num_expenses):
    expenses.append(float(input('Enter an expense: ')))

total = sum(expenses)
print(f"You spent $ {total}")
