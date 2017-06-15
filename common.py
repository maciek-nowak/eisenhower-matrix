from datetime import datetime


def choose_quarter_name(deadline, is_important):
    current_date = datetime.today()

    if (deadline - current_date).days <= 3:
        urgency = 'U'
    else:
        urgency = 'N'

    importancy = {True: 'I', False: 'N'}
    quarter_name = importancy[is_important] + urgency

    return quarter_name


def read_file(file_name):
    with open(file_name) as datafile:
        item_list = datafile.readlines()
    return item_list


def prepare_items_to_add(item_list):
    item_list = [item.strip().split('|') for item in item_list]

    importancy = {'important': True, '': False}
    for i in range(len(item_list)):
        item_list[i][1] = item_list[i][1].split('-')
        item_list[i][1] = datetime(2017, int(item_list[i][1][1]), int(item_list[i][1][0]))
        item_list[i][2] = importancy[item_list[i][2]]
    return item_list


def create_list_to_save(matrix):
    list_to_save = []
    importancy = {'I': 'important', 'N': ''}

    for key in matrix.todo_quarters:
        for item in matrix.todo_quarters[key].todo_items:
            list_to_save.append([item.title, item.deadline, importancy[key[0]]])

    return list_to_save


def prepare_items_to_save(list_to_save):
    list_to_save = [[item[0], str(item[1].day) + '-' + str(item[1].month), item[2]] for item in list_to_save]
    list_to_save = ['|'.join(item) + '\n' for item in list_to_save]
    return list_to_save


def prepare_titles_row(columns_width):
    titles_row = '  |' + 'URGENT'.center(columns_width) + '|' + 'NOT URGENT'.center(columns_width) + '|  '
    return titles_row


def prepare_border_row(columns_width):
    border_row = '--|' + '-' * columns_width + '|' + '-' * columns_width + '|--'
    return border_row


def prepare_important_rows(str_list, columns_width, rows_height, row_name):
    iu_list = str_list[0].strip().splitlines()
    in_list = str_list[1].strip().splitlines()

    if len(iu_list) < rows_height:
        iu_list += ['' for i in range(rows_height - len(iu_list))]
    if len(in_list) < rows_height:
        in_list += ['' for i in range(rows_height - len(in_list))]

    list_to_print = []
    row_name = row_name.center(rows_height)

    for i in range(rows_height):
        single_row = row_name[i] + ' | ' + iu_list[i].ljust(columns_width - 1) + '| ' + in_list[i].ljust(
            columns_width - 1) + '|  '
        list_to_print.append(single_row)

    important_rows = '\n'.join(list_to_print)
    return important_rows
