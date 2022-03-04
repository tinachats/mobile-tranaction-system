import os 

# Check if mobile number exists
def check_mobile_number(mobile_number):
    phone_exist = False
    if os.path.exists('userDB.txt'):
        with open('userDb.txt', 'r') as f:
            if mobile_number in f.read():
                phone_exist = True 
    else:
        open('userDB.txt', 'a')

    return phone_exist

# Register new user in the userDB if mobile number 
# doesn't exist
def register_user(users):
    with open('userDB.txt', 'a') as f:
        if len(users) > 0:
            for user in users:
                f.write('%s\n' % user)
        else:
            f.write('%s\n', users)
