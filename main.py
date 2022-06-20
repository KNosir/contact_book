from modules_for_project import *
breaking_the_loop = True


while breaking_the_loop:
    command = input('Type help to see commands list: ')

    if command.lower() == 'add':
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        email = input('Enter email: ')
        writing_file(name, phone, email)
    elif command.lower() == 'search':
        pass
    elif command.lower() == 'exit':
        print('')
        print(f'-----------')
        print(f'See later ')
        print(f'-----------')
        print('')
        breaking_the_loop = False
    elif command.lower() == 'help':
        print(
        '''
        "search" for seacrching.
        "add" to add new contact.
        "exit" if you want to exit
        "contacts" all contacts list in table
        "help" commands list
        '''
        )
    else:
        print('')
        print(f'-----------')
        print(f'Try to type correctly')
        print(f'-----------')
        print('')
    