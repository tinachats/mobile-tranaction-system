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
    
    @property
    # Give the user an email address 
    def email(self):
        return '{}.{}@mobitransys.com'.format(self.first_name.lower(), self.last_name.lower())

    # The user object
    def user_data(self):
        obj = {
            "first_name": self.first_name, 
            "last_name": self.last_name, 
            "mobile_number": self.mobile_number, 
            "wallet_balance": self.wallet_balance, 
            "age": self.age, 
            "gender": self.gender, 
            "pin": self.pin
        }
        return obj
    
    # Special methods
    # Represent the user object
    def __repr__(self):
        return "User('{}', '{}', '{}', {}, {}, '{}', '{}')".format(self.first_name, self.last_name, 
    self.mobile_number, self.wallet_balance, self.age, self.gender, self.pin)

    # Show data to the client
    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.first_name, self.last_name, 
        self.mobile_number, self.wallet_balance, self.age, self.gender, self.pin)

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

        # Create a user instance
        user = User(first_name, last_name, mobile_number,
        wallet_balance, age, gender, pin)

        # Verify if user info is correct
        user.verify(pin, mobile_number)

        # save the user in the text file
        mobile_number = mobile_number
        pin = pin

        # Create a files instance for creating the 
        # user database
        files = Files('userDB.json')
        
        # Check if number is not already registered
        while files.check_mobile_number(mobile_number):
            print(f'{mobile_number} already registered with us. Try a different one.')
            mobile_number = input('Enter different mobile number: ')
            user.mobile_number = mobile_number

        # Save user details
        # users.append(user.user_data()) # Create a list of objects
        # users.append(user) # Create a list object based on the user instance
        
        user_info = user.user_data()
        files.save_user(user_info)
        
        # Show the results to the user
        print(repr(user))
        print(user)

    def login():
        print('Login into your account')
        max_trials = 3
        attempts = 0

        # Create a files instance
        files = Files('userDB.json')

        pin = input('Enter your 4-digit pin: ')
        mobile_number = input('Enter your mobile number: ')

        while attempts < max_trials:
            # Fetch all user info from the database
            users = []

            if files.check_pin(pin) and files.check_mobile_number(mobile_number):
                users = [
                    {
                        'first_name': 'tinashe', 
                        'last_name': 'chaterera', 
                        'mobile_number': '0776021140', 
                        'wallet_balance': 38348.0, 
                        'age': 30, 
                        'gender': 'm', 
                        'pin': '0000'
                    }, 
                    {
                        'first_name': 'jane', 
                        'last_name': 'doe', 
                        'mobile_number': '0774729412', 
                        'wallet_balance': 3848.0, 
                        'age': 39, 
                        'gender': 'm', 
                        'pin': '0001'
                    }
                ]

                # Get user info
                for user in users:
                    if user['mobile_number'] == mobile_number and user['pin'] == pin:
                        print(user)
                        break

                print('Welcome {}!'.format(user["first_name"].title()))
                break 
            else:
                print('Incorrect pin or mobile number. Try again.')
                pin = input('Enter your 4-digit pin: ')
                mobile_number = input('Enter your mobile number: ')
                attempts += 1
                attempts_left = max_trials - attempts
                output = ''

                if attempts_left == 1:
                    output = '1 attempt left.'
                else:
                    output = '{} attempts left.'.format(attempts_left)

                print(output)
        else: 
            print('You\'ve exhausted your number of trials.')
            User.quit_program()
    
    @staticmethod 
    def quit_program():
        option = input('Do you want to exit? (Y / n): ')

        if option in ['Yes', 'yes', 'Y', 'y', 'yep']:
            print('Exiting...')
            quit()



