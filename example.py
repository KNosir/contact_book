from tabulate import tabulate
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


result = separated_file_into_list_by_dic()

print(tabulate(result, headers='firstrow', tablefmt='grid'))