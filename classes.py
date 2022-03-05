class User:
    # Class Variables
    user_id = 0

    # Create the user class with the given attributes
    def __init__(self, user_id, first_name, last_name, mobile_number, age, gender, wallet_balance, pin):
        user_id += 1
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.age = age
        self.gender = gender
        self.wallet_balance = wallet_balance
        self.pin = pin 

    # Regular method 
    def user_greeting(self):
        import datetime as dt 
        hour = dt.datetime.now().hour 
        greeting = ''
        if hour >= 0 and hour < 12:
            greeting = 'Good morning, {}!'.format(self.first_name)
        elif hour >= 12 and hour < 18:
            greeting = 'Good afternoon, {}!'.format(self.first_name)
        else:
            greeting = 'Good evening, {}!'.format(self.first_name)

        print(greeting)

    @staticmethod 
    def from_file_objects(filename, mode):
        import os 
        if os.path.exists(filename):
            with open(filename, mode) as f:
                for line in f:
                    data = line.split('"') 
                    return data
        else:
            print('File not found.')
    
user_data = User.from_file_objects('userDB.txt', 'r')
    
user1 = User(0, 'tinashe', 'chaterera', '0776021140', 30, 'male', 300, 3948)
user2 = User(1, 'marshall', 'chats', '0774729412', 29, 'male', 500, 3849)
user3 = User(2, 'tatiana', 'hemsworth', '0777735259', 25, 'female', 1000, 1812)
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
user1.user_greeting()