import ast


def writing_file(name, phone, email):
    """This function for adding new contact name phone and email"""
    f = open('data.txt', 'a')
    bracket_left = '{'
    bracket_right = '}'
    quote = '"'
    adding = (f'{bracket_left}{quote}name{quote}:{quote}{name}{quote}, {quote}phone{quote}:{quote}{phone}{quote}, {quote}email{quote}:{quote}{email}{quote}{bracket_right}')
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
    free_dict_list = []

    for i in read_f_list:
        if len(i) > 5:
            i = ast.literal_eval(i)
            free_dict_list.append(i)
    return free_dict_list
