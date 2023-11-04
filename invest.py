def invest(principal,  rate, year):
    for i in range(1,year+1):
        end_of_year = principal + (principal * rate / 100)
        principal = end_of_year
        print(f"Year {i} :  ${principal: .2f}")

principal = input("Enter initial amount to save ")
rate = input("Enter the rate in percentage ")
year = input("Enter the number of years ")


investment = invest(float(principal),float(rate),int(year))

