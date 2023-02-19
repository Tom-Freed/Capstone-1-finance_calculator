import math

# Ask the user to choose which calculator they want to user
while True:
    choice = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

        investment  -  to calculate the amount of interest you'll earn on your investment
        bond        -  to calculate the amount you'll have to pay on a home loan
        
        """).lower()
        
    # Investment calculator
    if choice == "investment":
       
        # To record the deposit amount, it will repeat until only numbers are entered
        while True:
            try:
                deposit = float(input("Please enter the amount of money you are depositing - no currency symbols: "))
                break
            except:
                print("Please only enter numbers")
                pass
       
         # To record the interest rate and divide by 100 to calculate decimal, it will repeat until only numbers are entered
        while True:
            try:
                interest_rate = float(input("Please enter the interest rate to be used - numbers only no '%' needed: "))/100
                break
            except:
                print("Please only enter numbers")
                pass
       
        # To record the number of years, it will repeat until only numbers are entered
        while True:
            try:
                num_years = float(input("Please enter the number of years you plan to invest for: "))
                break
            except:
                print("Please only enter numbers")
                pass
       
        # To record whether simple or compound interest will be used, it will repeat until simple or compound is entered
        while True:
            interest = input("Please enter either 'simple' or 'compound' for the type of interest you would like: ").lower()
            # To calculate and output the total return for simple interest
            if interest == "simple":
                total_amount = deposit * (1 + interest_rate * num_years)
                break
            # To calculate and output the total return for compound interest
            elif interest == "compound":
                total_amount = deposit * math.pow((1 + interest_rate), num_years)
                break
            # To repeat if simple or compound is not entered
            else:
                pass
        
        # To determine the currency being used
        currency = input("Please enter the symbol of the currency you wish to use, e.g. R or £: ")
        
        # Output the total return with the selected currency symbol to 2 decimal places
        print (f"The total amount you will recieve back from this investment will be: {currency}{total_amount:.2f}")
        break


    # Bond calculator    
    elif choice == "bond":

        # To record the value of the house, it will repeat until only numbers are entered
        while True:
            try:
                value_house = float(input("Please enter the value of the house - no currency symbol needed: "))
                break
            except:
                print("Please only enter numbers")
                pass
        
        # To record the interest rate and divide by 100 to calculate decimal, it will repeat until only numbers are entered
        while True:
            try:
                interest_rate = float(input("Please enter the interest rate to be used - numbers only no '%' needed: "))/100
                break
            except:
                print("Please only enter numbers")
                pass

        # To record the number of months the bond will be repaid over, it will repeat until only numbers are entered
        while True:
            try:
                num_months = float(input("Please enter the number of months you plan repay the bond over: "))
                break
            except:
                print("Please only enter numbers")
                pass
        
        # To determine the currency being used
        currency = input("Please enter the symbol of the currency you wish to use, e.g. R or £: ")

        # Monthly interest rate calculated here instead of at the input to conserve original interest rate
        monthly_interest_rate = interest_rate/12

        # To calculate the monthly repayment amount and output the monthly repayment amount with the currency symbol to 2 decimal places
        monthly_repayment = (monthly_interest_rate * value_house) / (1 - (1 + monthly_interest_rate) ** -abs(num_months))
        print(f"The monthly repayment amount of your bond will be: {currency}{monthly_repayment:.2f}")
        break


    # Error message if neither investment or bond are entered
    else:
        print("Please enter either 'investment' or 'bond'.")
        pass
    