blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if(last_transaction == None):
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Your choice')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputing block')
        print(block)


def print_options():
    print('Please chose')
    print('1: Add new transaction value')
    print('2: Output the blocks')
    print('h: Manipulate the chain')
    print('q: Quit')


while True:
    print_options()
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Invalid command. Please chose one from the list')
    print('Choice registered!')

print('Done!')
