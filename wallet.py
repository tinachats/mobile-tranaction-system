from users import *
from datetime import datetime as dt

class Wallet(User):
    def __init__(self, first_name, last_name, mobile_number, wallet_balance, age, gender, pin, sent_amount, transaction_date, friends=None, friends_number=None):
        super().__init__(first_name, last_name, mobile_number, wallet_balance, age, gender, pin)
        self.sent_amount = sent_amount
        self.transaction_date = transaction_date
        if friends is None:
            self.friends = []
        else:
            self.friends = friends 

        if friends_number is None:
            self.friends_number = []
        else:
            self.friends_number = friends_number

    def send_money(self):
        print('Send money from your account') 
        return '{} sent to {}. Sent on {}.'.format(self.sent_amount, self.friends_number, self.transaction_date)

    def balance_enquiry(self):
        print('Check your balance')
        return 'Available ${}'.format(self.wallet_balance)