from users import *
# Registering new users
def user_input():
    user_id = 0
    first_name = input('Enter your first name: ').title()
    last_name = input('Enter your last name: ').title()
    mobile_number = input('Enter your mobile phone number: ')
    age = int(input('Enter your age: '))
    gender = input('Enter your gender (M / F): ').capitalize()
    wallet_balance = round(float(input('Enter your bank balance: ')), 2)
    pin = input('Enter your 4 digit PIN: ')

    # Create an incrementing user_id for every registed user

    # Combine user data
    user_data = {
        'user_id': user_id,
        'first_name': first_name, 
        'last_name': last_name, 
        'mobile_number': mobile_number, 
        'age': age, 
        'gender': gender, 
        'wallet_balance': wallet_balance, 
        'pin': pin
    }

    return user_data

