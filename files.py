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
                    # Register your account
                    print('Account successfully created!')
                    break
            else:
                # Register your account
                print('Account successfully created!')
                file.write('%s\n' % users)
            
    # Check if the mobile number is not already registered
    def check_mobile_number(self, mobile_number):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                if mobile_number in file.read():
                    return True
        else:
            open(self.filename, 'a')

    # Check if the mobile number is not already registered
    def check_pin(self, pin):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                if pin in file.read():
                    return True
        else:
            open(self.filename, 'a')

    # Getting the data in a file into a list
    def file_to_list(self, arr):
        arr = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.replace('"', "").strip()
                    arr.append(data) 
                print(arr)
        