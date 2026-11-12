loan_amount = float(input("Enter the loan amount: "))
years = int(input("Enter the number of years: "))
months = years * 12
principal = loan_amount / months
remaining_balance = loan_amount

total = 0
print("| MONTH\t|\tPAYMENT\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t|")
for x in range(1, months + 1):
    remaining_balance -= principal
    loan_interest = remaining_balance * 0.00259
    monthly_payment = principal + loan_interest
    total += loan_interest
    print(f"|    {x}\t|\t{round(monthly_payment, 2)}\t|\t{round(loan_interest, 2)}\t\t|\t{round(principal, 2)}\t\t|\t{round(remaining_balance, 2)}\t|")

print(total)
