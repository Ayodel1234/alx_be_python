monthly_income = float(input("Enter your monthly income: "))
annual_income = monthly_income * 12
monthly_expenses = float(input("Enter your total monthly expenses: "))
annual_expenses = monthly_expenses * 12
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print ("Your monthly savings are: $" + str(monthly_savings))
print ("Projected savings after one year, with interest, is: $" + str(projected_savings))