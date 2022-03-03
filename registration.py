# Import the user inputs function 
# from the user_inputs module
from user_inputs import userInput

# Register new users
def userRegistration():
    # Create a users array to hold all users
    users = []

    # Fetch user data if it's available
    user_data = userInput()

    # Keep prompting the user to enter the correct pin if they have enter a wrong
    # pin and password
    # while len(user_data.pin) != 4 or len(user_data.mobile_number) != 10:
    #     pass

    # Register the user if and only if the pin is correct and the mobile number
    if user_data.mobile_number.isdigit() and user_data.pin.isdigit():
        if len(user_data.pin) == 4 and len(user_data.mobile_number) == 10:
            # Check to see if the mobile number already exists
            if len(users) > 0:
                for user in users:
                    if user.mobile_number == user_data.mobile_number:
                        print('Mobile number already registered! Try another one.');
                    else: 
                        users.append(user_data)
                        print(f'Welcome { user_data.first_name }!')
            else:
                users.append(user_data)
                print(f'Welcome { user_data.first_name }!')
        elif len(user_data.pin) != 4:
            print('Your pin is incorrect!')
        elif len(user_data.mobile_number) != 10:
            print('Mobile number is incorrect!')
        else:
            pass