
#Payroll Wages calculator 

hours_worked=float(input("how many hours do you work per day?"))
hourly_pay=float(input("what is your hourly pay?"))
days_worked=float(input("how many days per week do you work"))


total_pay=hours_worked*hourly_pay*days_worked

print("this is your total weekly pay",total_pay)