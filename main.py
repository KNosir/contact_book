from tabulate import tabulate
breaking_the_loop = True


def writing_file(name, phone, email):
    """This function for adding new contact name phone and email"""
    f = open('data.txt', 'a')
    bracket_left = '['
    bracket_right = ']'
    quote = '"'
    adding = (f'{bracket_left}{quote}{name}{quote}, {quote}{phone}{quote}, {quote}{email}{quote}{bracket_right}')
    f.write('|' + adding + '|'+'\n')
    f.close

def reading_file():
    """Reading file """
    f = open('data.txt', 'r')
    return f.read()

def separated_file_into_list_by_dic():
    '''Separating text into list by dic element'''
    f = open('data.txt', 'r')
    read_f = f.read()
    read_f_list = read_f.split('|')
    free_list = []
    for i in read_f_list:
        if len(i) > 2:
            i = list(map(str.strip, i.strip('][').replace('"', '').split(',')))
            free_list.append(i)
    free_list.insert(0, ['Name', 'Phone number', 'E-mail'])

    return free_list

def show_contact_in_table():
    result = separated_file_into_list_by_dic()
    print(tabulate(result, tablefmt='grid'))

def searching(key_word):
    for item in separated_file_into_list_by_dic():
        result_list = []
        if key_word in item:
            result_list.append(item)
    print(tabulate(result_list, floatfmt='grid'))

        


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