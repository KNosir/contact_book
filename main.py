from tabulate import tabulate
breaking_the_loop = True

#add
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
#contacts
def show_contact_in_table():
    result = separated_file_into_list_by_dic()
    print(tabulate(result, tablefmt='psql', headers='firstrow', showindex='always'))

def searching(key_word): 
    result_list = []
    for item in separated_file_into_list_by_dic():
        if key_word.lower() in ''.join(item).lower():
            result_list.append(item)
    result_list.insert(0, ['Name', 'Phone Number', 'E-mail'])
    print(tabulate(result_list, headers='firstrow', floatfmt='grid', showindex='always'))

        


while breaking_the_loop:
    command = input('Type help to see commands list: ')
    #completed
    if command.lower() == 'add': 
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        email = input('Enter email: ')
        writing_file(name, phone, email)
    #completed
    elif command.lower() == 'search':  
        search_input = input('Input key word to search: ')
        searching(search_input)
    #completed
    elif command.lower() == 'exit':
        print('')
        print(f'-----------')
        print(f'See later ')
        print(f'-----------')
        print('')
        breaking_the_loop = False
    #completed
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
    #completed
    elif command.lower() == 'contacts':
        show_contact_in_table()
    # elif command.lower() == 'delete':
    #     index = int(input('Input the index for del: '))
    #     index += 1
    #     deleted_list_index = []
    #     deleted_list_index.append(index)
    #     print(deleted_list_index)
    
    #completed Incorrect input part
    else:
        print("""

        ---------------------
        Incorrect word!!!
        For more information 
            type "help"
        ---------------------

        """)