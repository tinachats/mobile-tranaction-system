# Created the User class
class User:
    # Created the object
    def __init__(self, first_name, last_name, age, gender, bank_balance, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.bank_balance = bank_balance
        self.pin = pin

    # Registering new users
    def userInput(self):
        self.first_name = input('Enter your first name: ').title()
        self.last_name = input('Enter your last name: ').title()
        self.age = int(input('Enter your age: '))
        self.gender = input('Enter your gender (M / F): ').capitalize()
        self.bank_balance = round(float(input('Enter your bank balance: ')), 2)
        self.pin = input('Enter your 4 digit PIN: ')

        # Combine user data
        user_data = User(self.first_name, self.last_name, self.age, self.gender, self.bank_balance, self.pin)

        return user_data

    # Pin validation
    def validPin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            print('Registered!')
        else:
            print('Invalid pin format.')
