from user_inputs import *
from file_mgt import *

# Register new users
def user_registration():
    print('Hello! Sign up, it\'s free.')

    # Create a users array to hold all users
    users = []

    # Fetch user data if it's available
    user_data = user_input()

    # Register the user if and only if the pin 
    # is correct and the mobile number
    if user_data['mobile_number'].isdigit() and user_data['pin'].isdigit():
        if len(user_data['pin']) == 4 and len(user_data['mobile_number']) == 10:
            # Check to see if the mobile number already exists
            if check_mobile_number(user_data['mobile_number']):
                print('Account already exist. Please login.')
            else:
                users.append(user_data) 
                register_user(users)
        elif len(user_data['pin']) != 4:
            print('Your pin is incorrect!')
        elif len(user_data['mobile_number']) != 10:
            print('Mobile number is incorrect!')
        else:
            pass

# Login functionality
def login():
    print('Login to enjoy mobile transaction services.')

    mobile_number = input('Enter your mobile phone number: ')
    pin = input('Enter your 4 digit pin: ')

    if check_mobile_number(mobile_number) and verify_pin(pin):
        print('Welcome back!')
    else:
        print('Mobile number or pin is incorrect. Try again.')

    print(auth_details(mobile_number))

# Send money
def send_money():
    print('Send money')

# Balance enquiry
def balance_enquiry():
    print('Balance enquiry')
    print(f'Your wallet balance is $384.48.')