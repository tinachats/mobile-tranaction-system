# Validate phone and pin
def validate(field, limit):
    if field.isdigit() and len(field) == limit:
        return True
    else: 
        return False

def verify(pin, mobile_number):
    while validate(pin, 4) != True or validate(mobile_number, 10) != True:
        if validate(pin, 4) != True:
            print('Pin is incorrect!')
            pin = input('Enter your 4 digit pin: ')
        if validate(mobile_number, 10) != True:
            print('Mobile number is incorrect!') 
            mobile_number = input('Enter your mobile number: ')
    else:
        # Register your account
        print('Account successfully created!')
