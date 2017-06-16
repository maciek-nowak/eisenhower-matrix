from datetime import datetime


def choose_quarter_name(deadline, is_important):
    """
    Function chooses quarter of matrix

    Args:
        deadline (obj): object of datetime class
        is_important (bool)

    Returns:
        quarter_name (str): name of matrix quarter
    """

    current_date = datetime.today()

    if (deadline - current_date).days < 3:
        urgency = 'U'
    else:
        urgency = 'N'

    importancy = {True: 'I', False: 'N'}
    quarter_name = importancy[is_important] + urgency

    return quarter_name


def read_file(file_name):
    """
    Function reads file content

    Args:
        file_name (str): name of the file

    Returns:
        item_list (list of str): list of file lines
    """

    with open(file_name) as datafile:
        item_list = datafile.readlines()
    return item_list


def prepare_items_to_add(item_list):
    """
    Function prepares data format for adding new TodoItem objects

    Args:
        item_list (list of str): list of file lines
            (function changes list content)

    Returns:
        item_list (list of lists): inner lists [str, datetime obj, bool]
    """

    item_list = [item.strip().split('|') for item in item_list]

    importancy = {'important': True, '': False}
    for i in range(len(item_list)):
        item_list[i][1] = item_list[i][1].split('-')
        item_list[i][1] = datetime(2017, int(item_list[i][1][1]), int(item_list[i][1][0]))
        item_list[i][2] = importancy[item_list[i][2]]
    return item_list


def create_list_to_save(matrix):
    """
    Function creates data of all TodoItems to export to the file

    Args:
        matrix (obj): object represents whole Eisenhower Matrix

    Returns:
        list_to_save (list of lists): inner lists [str, datetime obj, bool]
    """

    list_to_save = []
    importancy = {'I': 'important', 'N': ''}

    for key in matrix.todo_quarters:
        for item in matrix.todo_quarters[key].todo_items:
            list_to_save.append([item.title, item.deadline, importancy[key[0]]])

    return list_to_save


def prepare_items_to_save(list_to_save):
    """
    Function prepares list of strings to save to the file

    Args:
        ist_to_save (list of lists): inner lists [str, datetime obj, bool]
            (function changes list content)

    Returns:
        item_list (list of strings): list of strings to save
    """

    list_to_save = [[item[0], str(item[1].day) + '-' + str(item[1].month), item[2]] for item in list_to_save]
    list_to_save = ['|'.join(item) + '\n' for item in list_to_save]
    return list_to_save


def prepare_titles_row(columns_width):
    """
    Function prepares title row of matrix to print

    Args:
        columns_width (int): width of matrix quarters

    Returns:
        titles_row (str): title row of matrix to print
    """

    titles_row = '  |' + 'URGENT'.center(columns_width) + '|' + 'NOT URGENT'.center(columns_width) + '|  '
    return titles_row


def prepare_border_row(columns_width):
    """
    Function prepares border row of matrix to print

    Args:
        columns_width (int): width of matrix quarters

    Returns:
        border_row (str): border row of matrix to print
    """

    border_row = '--|' + '-' * columns_width + '|' + '-' * columns_width + '|--'
    return border_row


def prepare_important_rows(str_list, columns_width, rows_height, row_name):
    """
    Function prepares data rows of matrix to print

    Args:
        str_list (list of lists): lists of quarters texts
        columns_width (int): width of matrix quarters
        rows_height (int): height of matrix quarters
        row_name (str): name of maatrix data row

    Returns:
        important_row (str): data row of matrix to print
    """

    iu_list = str_list[0].strip().splitlines()  # first column text
    in_list = str_list[1].strip().splitlines()  # second column text

    # if column is too short blank lines are being added to the end
    if len(iu_list) < rows_height:
        iu_list += ['' for i in range(rows_height - len(iu_list))]
    if len(in_list) < rows_height:
        in_list += ['' for i in range(rows_height - len(in_list))]

    list_to_print = []
    row_name = row_name.center(rows_height)

    # creating list of data strings to print
    for i in range(rows_height):
        colored_iu = iu_list[i]
        colorless_iu = colored_iu.replace('\033[0m', '').replace('\033[31m', '').replace('\033[32m', '').replace(
            '\033[33m', '')
        colored_in = in_list[i]
        colorless_in = colored_in.replace('\033[0m', '').replace('\033[31m', '').replace('\033[32m', '').replace(
            '\033[33m', '')

        # creating row from colorless data (needed for proper text justification)
        single_row = row_name[i] + ' | ' + colorless_iu.ljust(columns_width - 1) + '| ' + colorless_in.ljust(
            columns_width - 1) + '|  '

        # substitutes colorless data into colored data
        single_row = single_row.replace(colorless_iu, colored_iu).replace(colorless_in, colored_in)

        list_to_print.append(single_row)

    # joins list of strings into single string
    important_rows = '\n'.join(list_to_print)
    return important_rows


def print_error_message(message):
    """
    Function prints red error message

    Args:
        message (str): error message to print

    Returns:
        None
    """

    RESET_COLOR = '\033[0m'
    RED = '\033[31m'

    print(RED + message + RESET_COLOR)


def choose_item_color(deadline):
    """
    Function chooses proper color

    Args:
        deadline (obj): object of datetime class

    Returns:
        color (str): escape code for terminal color
    """

    RED = '\033[31m'
    ORANGE = '\033[33m'
    GREEN = '\033[32m'

    time_to_deadline = (deadline - datetime.today()).days
    if time_to_deadline < 0:
        color = RED
    elif time_to_deadline < 3:
        color = ORANGE
    else:
        color = GREEN

    return color
