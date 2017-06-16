import common
from datetime import datetime


def add_item(matrix):
    """
    Function gets input from user and adds item to the matrix

    Args:
        matrix (obj): object represents whole Eisenhower Matrix
                        (function changes the object)

    Returns:
        None
    """
    item_name = ''
    while not len(item_name) or len(item_name) == item_name.count(' '):
        item_name = input('Type name of the item to add (max 50 characters): ')

    if len(item_name) > 50:
        item_name = item_name[:50]

    print('Type the deadline of the item: ')
    month = ''
    while not month.isdigit() or int(month) not in range(1, 13):
        month = input('Type the number of the month [1 - 12]: ')
        if not month.isdigit() or int(month) not in range(1, 13):
            common.print_error_message('Month has to be in range [1 - 12]')

    is_day_correct = False
    while not is_day_correct:
        is_day_correct = True

        day = ''
        while not day.isdigit() or int(day) not in range(1, 32):
            day = input('Type the number of the day [1 - 31]: ')
            if not day.isdigit() or int(day) not in range(1, 32):
                common.print_error_message('Day has to be in range [1 - 31]')

        try:
            deadline = datetime(2017, int(month), int(day))
        except ValueError:
            common.print_error_message('Incorrect day for given month')
            is_day_correct = False

    is_important = ''
    while is_important not in ['y', 'n']:
        is_important = input('Is this task important [y / n]: ')

    importancy = {'y': True, 'n': False}

    try:
        matrix.add_item(item_name, deadline, importancy[is_important])
    except TypeError:
        common.print_error_message('The deadline format is not proper!')


def choose_quarter(matrix):
    """
    Function gets input from user and chooses the proper quarter of matrix

    Args:
        matrix (obj): object represents whole Eisenhower Matrix

    Returns:
        (obj): object represents chosen quarter of matrix
    """

    choose_quarter_dict = {1: 'IU', 2: 'IN', 3: 'NU', 4: 'NN'}
    choose_quarter_menu = """Choose the quarter of matrix:
    1. Important & urgent
    2. Important & not urgent
    3. Not important & urgent
    4. Not important & not urgent
    ╔═══╦═══╗
    ║ 1 ║ 2 ║
    ╠═══╬═══╣
    ║ 3 ║ 4 ║
    ╚═══╩═══╝"""

    print(choose_quarter_menu)

    user_input = ''
    while user_input not in ['1', '2', '3', '4']:
        user_input = input('Your choice: ')
        if user_input not in ['1', '2', '3', '4']:
            common.print_error_message('Quarter number has to be in range [1 - 4]')

    return matrix.get_quarter(choose_quarter_dict[int(user_input)])


def choose_item(chosen_quarter):
    """
    Function gets input from user and chooses the proper item of given matrix quarter

    Args:
        chosen_quarter (obj): object represents one of the Eisenhower Matrix quarters

    Returns:
        chosen_item (obj): object represents chosen item of TodoItem class
    """

    user_input = ''
    while not user_input.isdigit():
        user_input = input('Choose number of item: ')

    chosen_item = chosen_quarter.get_item(int(user_input) - 1)

    return chosen_item


def choose_item_index():
    """
    Function gets input from user and returns index of item

    Returns:
        chosen_item_index (int): number chosen by user
    """

    user_input = ''
    while not user_input.isdigit():
        user_input = input('Choose number of item: ')

    chosen_item_index = int(user_input) - 1

    return chosen_item_index


def mark_item(matrix):
    """
    Function marks item as done

    Args:
        matrix (obj): object represents whole Eisenhower Matrix
                    (function changes the one of TodoItem object attributes)
    Returns:
        None
    """

    chosen_quarter = choose_quarter(matrix)

    try:
        chosen_item = choose_item(chosen_quarter)
        chosen_item.mark()
    except IndexError:
        common.print_error_message('There is no such item!')


def unmark_item(matrix):
    """
    Function marks item as undone

    Args:
        matrix (obj): object represents whole Eisenhower Matrix
                    (function changes the one of TodoItem object attributes)
    Returns:
        None
    """

    chosen_quarter = choose_quarter(matrix)

    try:
        chosen_item = choose_item(chosen_quarter)
        chosen_item.unmark()
    except IndexError:
        common.print_error_message('There is no such item!')


def remove_item(matrix):
    """
    Function removes item from quarter list of items

    Args:
        matrix (obj): object represents whole Eisenhower Matrix
                    (function removes one of the TodoItem class objects)
    Returns:
        None
    """

    chosen_quarter = choose_quarter(matrix)
    chosen_item_index = choose_item_index()

    try:
        chosen_quarter.remove_item(chosen_item_index)
    except IndexError:
        common.print_error_message('There is no such item!')
