# Created the User class
class User:
    # Created the object with the following attributes
    def __init__(self, first_name, last_name, mobile_number, age, gender, wallet_balance, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.age = age
        self.gender = gender
        self.wallet_balance = wallet_balance
        self.pin = pin

# Get the user's username
def username():
    import os
    username = os.getlogin()
    return username 

# User timely greeting
def greeting():
    import datetime as dt

    # Get the hour
    hour = dt.datetime.now().hour
    
    greeting = ''

    if hour > 0 and hour < 12:
        greeting = f'Good morning, {username()}!'
    elif hour > 12 and hour < 18:
        greeting = f'Good afternoon, {username()}! '
    else: 
        greeting = f'Good evening, {username()}!'

    return greeting

