# Function to register new users
def registration(first_name, last_name, age, gender, bank_balance, pin):
    users = []
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = int(input('Enter your age: '))
    gender = input('Enter your gender: ')

    user = {
        first_name: first_name,
        last_name: last_name,
        age: age,
        gender: gender,
        bank_balance: bank_balance,
        pin: pin
    }

    users.append(user)

# Make sure the pin entered is a valid 4-digit pin
def pin():
    pin = 0
    entered_pin = input('Enter your 4 digit pin: ')

    # Make sure the pin is within the range 0 - 10000
    # and it's a 4 digit pin
    if entered_pin.isdigit() and entered_pin in range(0000, 10000) and len(entered_pin) == 4:
        pin = entered_pin
    else:
        return False
