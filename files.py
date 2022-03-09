import os 
from users import *

class Files:
    def __init__(self, filename):
        self.filename = filename

    # Function for saving registered users
    def save_user(self, users):
        with open(self.filename, 'a') as file:
            if len(users) > 0:
                for user in users:
                    file.write('%s\n' % user)
                    break
            else:
                file.write('%s\n' % users)
            
    # Check if the mobile number is not already registered
    def check_mobile_number(self, mobile_number, users=None):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                if mobile_number in file.read():
                    print(f'{mobile_number} already registered with us. Try a different one.')
                else:
                    # Save the user
                    self.save_user(users)
        else:
            open(self.filename, 'a')
        