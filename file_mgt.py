# Manage files
import os
def userDB():
    path = '/users/audiozw.com/documents/python programs/userDB'
    # Check if the userDB folder already exists
    # if not create it
    if os.path.exists(path) == True:
        print('Folder exists.')
    else:
        os.makedirs(path)

userDB()