import users
# Registering new users
def userInput():
    first_name = input('Enter your first name: ').title()
    last_name = input('Enter your last name: ').title()
    mobile_number = input('Enter your mobile phone number: ')
    age = int(input('Enter your age: '))
    gender = input('Enter your gender (M / F): ').capitalize()
    bank_balance = round(float(input('Enter your bank balance: ')), 2)
    pin = input('Enter your 4 digit PIN: ')

    # Combine user data
    user_data = users.User(first_name, last_name, mobile_number, age, gender, bank_balance, pin)

    return user_data

