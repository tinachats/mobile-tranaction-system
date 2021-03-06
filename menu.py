from users import *
from wallet import *
import json

def menu():
    while True:
        try:
            print('SELECT YOUR OPTION!')
            print('1. Create your account.')
            print('2. Login into your account')
            print('3. Send money')
            print('4. Balance enquiry')
            print('5. Quit')

            option = int(input('Enter your menu option here: '))

            if option == 1:
                User.register_user()
            elif option == 2:
                # User.login()
                def fetch_data(mobile_number):
                    with open('userDB.json','r') as file:
                        text = file.read()
                        text = text.replace('\t','').replace('\n','')
                        text = text.replace(',}','}').replace(',]',']')
                        users = json.loads(text)
                    for user in users:
                        if mobile_number == user['mobile_number']:
                            print(user)
                            print(user['first_name'])
                fetch_data('0774729412')
            elif option == 3:
                Wallet.send_money()
            elif option == 4:
                Wallet.balance_enquiry()
            elif option == 5:
                User.quit_program()
            else: 
                print('Invalid menu option value')
        except ValueError as err:
            print(f'{err}')
