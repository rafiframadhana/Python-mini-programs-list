def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the number of years: "))

interest = compound_interest(principal, rate, time)

print("Compound interest after", time, "years is:", interest)
