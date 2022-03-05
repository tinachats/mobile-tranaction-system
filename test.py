def reg_test():
    user_id = 0
    user_data = {
        'user_id': user_id,
        'first_name': 'tinashe',
        'last_name': 'chaterera' + user_id,
        'mobile_number': '077' + user_id, 
        'age': 30 + user_id,  
        'gender': 'male' + user_id,  
        'wallet_balance': 300 + user_id,  
        'pin': '000' + user_id
    }
    
    return user_data

def choice():
    choice = input('Enter your choice: ')
    if choice == 1:
        i = 1
        users = []
        user_data = reg_test()

        for i in range(len(users)):
            users['user_id'] += i
            users.append(user_data)
        
        print(users)
    else: 
        pass

choice()