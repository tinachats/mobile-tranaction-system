from files import Files
from datetime import datetime as dt

class User:
    def __init__(self, first_name, last_name, 
    mobile_number, wallet_balance, age, gender, pin):
        self.first_name = first_name
        self.last_name = last_name 
        self.mobile_number = mobile_number
        self.wallet_balance = wallet_balance 
        self.age = age 
        self.gender = gender 
        self.pin = pin

    # Show the user's full name as a property 
    @property 
    def fullname(self):
        return '{} {}'.format(self.first_name.title(), self.last_name.title())

    # Set the fullname 
    @fullname.setter 
    def fullname(self, fullname):
        first_name, last_name = fullname.split(' ')
        self.first_name = first_name 
        self.last_name = last_name

    # Delete the user 
    @fullname.deleter
    def fullname(self):
        self.first_name = None 
        self.last_name = None

    # Give the user an email address 
    def email(self):
        return '{}.{}@mobitransys.com'.format(self.first_name.lower(), self.last_name.lower())

    # The user object
    def user_data(self):
        obj = {
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'mobile_number': self.mobile_number, 
            'wallet_balance': self.wallet_balance, 
            'age': self.age, 
            'gender': self.gender, 
            'pin': self.pin
        }
        return obj

    # Represent the user object
    def __repr__(self):
        return "User({}, '{}', '{}', '{}', {}, '{}', {})".format(self.first_name, self.last_name, 
    self.mobile_number, self.wallet_balance, self.age, self.gender, self.pin)

    # Show data to the client
    def __str__(self):
        return '{} - {} - ${}'.format(self.fullname, self.mobile_number, self.wallet_balance)

    # User greeting
    def user_greeting(self):
        hour = dt.now().hour
        greeting = ''
        if hour >= 0 and hour < 12:
            greeting = 'Good morning, {}!'.format(self.first_name.title())
        elif hour >= 12 and hour < 18:
            greeting = 'Good afternoon, {}!'.format(self.first_name.title())
        else:
            greeting = 'Good evening, {}!'.format(self.first_name.title())

        return greeting
    
    @staticmethod
    # Validate phone and pin
    def validate(field, limit):
        if field.isdigit() and len(field) == limit:
            return True
        else: 
            return False

    def verify(self, pin, mobile_number):
        while self.validate(pin, 4) != True or self.validate(mobile_number, 10) != True:
            if self.validate(pin, 4) != True:
                print('Pin is incorrect!')
                pin = input('Enter your 4 digit pin: ')
                
            if self.validate(mobile_number, 10) != True:
                print('Mobile number is incorrect!') 
                mobile_number = input('Enter your mobile number: ')

    # Register new user
    def register_user():
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        mobile_number = input('Enter your mobile number: ')
        wallet_balance = float(input('Enter your wallet balance: '))
        age = int(input('Enter your age: '))
        gender = input('Enter your gender (M / F): ')
        pin = input('Enter your 4-digit pin: ')
        users = []

        # Create a user instance
        user = User(first_name, last_name, mobile_number,
        wallet_balance, age, gender, pin)

         # Verify if user info is correct
        user.verify(pin, mobile_number)

        # save the user in the text file
        user.mobile_number = mobile_number
        user.pin = pin
        user_data = user.user_data()
        users.append(user_data)

        # Create a files instance for creating the 
        # user database
        files = Files('userDB.txt')
        
        # Check if number is not already registered
        while files.check_mobile_number(mobile_number):
            print(f'{mobile_number} already registered with us. Try a different one.')
            mobile_number = input('Enter different mobile number: ')
            user.mobile_number = mobile_number

        # Save user details
        files.save_user(users)
        
        # Show the results to the user
        print(repr(user))
        print(user)

    def login():
        print('Login into your account')
        max_trials = 3
        attempts = 0

        # Create a files instance
        files = Files('userDB.txt')

        while attempts < max_trials:
            pin = input('Enter your 4-digit pin: ')
            mobile_number = input('Enter your mobile number: ')
            
            # Fetch all users in the user database and populate 
            # the user array
            users = []

            if files.check_pin(pin) and files.check_mobile_number(mobile_number):
                # next((user for user in users if user['pin'] == '0001'), None)
                # for user in users:
                #     if user['pin'] == '0000':
                #         print('User found!')
                #         print(user)
                #         break
                # else:
                #     user = None
                files.file_to_list(users)

                print('Welcome user!')
                break 
            else:
                print('Incorrect pin or mobile number. Try again.')
                pin = input('Enter your 4-digit pin: ')
                mobile_number = input('Enter your mobile number: ')
                attempts += 1
                attempts_left = max_trials - attempts
                print(f'{attempts_left} attempts left.')
        else: 
            print('You\'ve exhausted your number of trials.')
    
    @staticmethod 
    def quit_program():
        print('Do you want to exit?')
