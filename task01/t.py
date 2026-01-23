while True:
    print("CLI PERSONAL FINANCE & EXPENSE TRACKER")

    print('1. Add Income \n2. Add Expense \n3. View financial summary \n4. View category-wise expense breakdown \n5. Search expenses \n6. Save data to file \n7. Load data from file \n8. Exit')

    menuOption = input('Choose Your Option: ')
    if menuOption == "1":
        income = []
        while True:            
            try:
                amount = float(input('Add Income: '))
                if amount > 0:
                    print('Income Added: %d' %amount)
                    income.append(amount)
                    break
                else:
                    print("income cannot be zero or negative ")
            
            except ValueError:
                print('entered wrong')
        
        while True:
            source = (input('Enter source of income \n(Choose "s" for Salary, "f" for Freelance, "b" for Bonus and "o" for Other): ')).lower()
            if source in ['s', 'f', 'b', 'o']:
                print('Source of income added %s' %source)
                break
            else:
                print('Choose from the options')
    
    elif menuOption == '8':
        print('Goodbye')
        break