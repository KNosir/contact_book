from tabulate import tabulate
from main import *
def searching(key_word):
    for item in separated_file_into_list_by_dic():
        result_list = []
        if key_word in item:
            result_list.append(item)
    print(tabulate(result_list, floatfmt='grid'))

searching(separated_file_into_list_by_dic())