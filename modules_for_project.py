from tabulate import tabulate


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