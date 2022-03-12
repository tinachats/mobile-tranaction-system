import os 
from users import *
import json
import ast

class Files:
    def __init__(self, filename):
        self.filename = filename

    # Function for saving registered users
    def save_user(self, user_info):
        with open(self.filename, 'a') as file:
            json.dump(user_info, file)
            file.write(',')
            print('Account successfully created!')
            
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

    # Getting the data in the userDB file into a list
    def file_to_list(self, mobile_number, pin):
        users = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding="utf-8") as file:
                for text in file:
                    users.append(text.replace('"', '').strip())

                # Get all the user info
                for user in users:
                    if user['mobile_number'] == mobile_number and user['pin'] == pin:
                        print(user)
                        break
                    else:
                        print(f'Hmmm... {mobile_number} not found!')
        