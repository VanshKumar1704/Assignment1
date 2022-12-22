gross_income=float(input("Enter your Gross Income = "))
dependents=float(input("Enter Number of Dependents ="))
taxable_income=gross_income-10000-(dependents*3000)
tax=taxable_income*20/100
print("Your Income Tax is =",tax)
