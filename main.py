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
        search_input = input()
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
        "add" to add new contact.
        "contacts" all contacts list in table
        "exit" if you want to exit
        "help" commands list
        "search" for seacrching.       
        '''
        )
    elif command.lower() == 'contacts':
        show_contact_in_table()
    else:
        print("""

        ---------------------
        Incorrect word!!!
        For more information 
            type "help"
        ---------------------

        """)