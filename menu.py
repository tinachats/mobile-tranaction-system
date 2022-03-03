def mainMenu():
    # Make the program run in an infinite loop
    while True:
        try:
            print('Welcome to Chaterera Mobile Services')
            print('PLEASE SELECT')
            print('1. Create an account.')
            print('2. Sign in')
            print('3. Send money')
            print('4. Check balance')
            print('5. Cancel')

            # Prompt the user to enter menu value
            menu_value = int(input('Enter your selection: \n'))

            if menu_value == 1:
                from registration import userRegistration
                print('Hello! Sign up, it\'s free.')
                userRegistration()
            elif menu_value == 2:
                print('Welcome back!')
            elif menu_value == 3:
                print('Send money')
            elif menu_value == 4:
                print('Balance enquiry')
            elif menu_value == 4:
                quit()
            else:
                print("Oops! That was no valid number. Try again...")
                continue
        except ValueError as err:
            print("Oops! That was no valid number. Try again...")
            print(f'Error type: { err }')

