from users import *

# Inheritance: Inherited the user class 
# This class gives a list of friends and friends' mobile numbers
# to select from when sending money
class Friend(User):
    def __init__(self, user_id, first_name, last_name, mobile_number, age, gender, wallet_balance, pin, friends=None, friends_number=None):
        super().__init__(user_id, first_name, last_name, mobile_number, age, gender, wallet_balance, pin)

        # Check whether the user has got friends
        if friends is None:
            self.friends = []
        else:
            self.friends = friends

        if friends_number is None:
            self.friends_number = []
        else:
            self.friends_number = friends_number
    
    # Special methods
    def __str__(self):
        return '{} - {} - {} - Friends:{}'.format(self.fullname, self.mobile_number, self.wallet_balance, self.friends)

    # Add a friend
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    # Remove a friend
    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    # List all your friends
    def list_friends(self):
        for friend in self.friends:
            print(friend.fullname)

    # List all your friends' phone numbers
    def list_friends_numbers(self):
        for friends_number in self.friends_numbers:
            print(friends_number)

friend1 = Friend(2, 'tatiana', 'hemsworth', '077429412', 29, 'female', 500, 1839, [])
print(repr(friend1))
print(str(friend1)) 
