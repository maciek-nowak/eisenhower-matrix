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
        item_name = input('Type name of the item to add: ')
    print('Type the deadline of the item: ')

    month = ''
    while not month.isdigit() or int(month) > 12 or int(month) < 1:
        month = input('Type the number of the month [1 - 12]: ')

    correct = False
    while not correct:
        correct = True

        day = ''
        while not day.isdigit() or int(day) > 31 or int(day) < 1:
            day = input('Type the number of the day [1 - 31]: ')

        try:
            deadline = datetime(2017, int(month), int(day))
        except ValueError:
            print('Incorrect day for given month')
            correct = False

    is_important = ''
    while is_important not in ['y', 'n']:
        is_important = input('Is this task important [y / n]: ')

    importancy = {'y': True, 'n': False}

    try:
        matrix.add_item(item_name, deadline, importancy[is_important])
    except TypeError:
        print('The deadline format is not proper!')


def choose_quarter(matrix):
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

    return matrix.get_quarter(choose_quarter_dict[int(user_input)])


def choose_item(chosen_quarter):
    user_input = ''
    while not user_input.isdigit():
        user_input = input('Choose number of item: ')

    chosen_item = chosen_quarter.get_item(int(user_input) - 1)

    return chosen_item


def choose_item_index():
    user_input = ''
    while not user_input.isdigit():
        user_input = input('Choose number of item: ')

    chosen_item_index = int(user_input) - 1

    return chosen_item_index


def mark_item(matrix):
    chosen_quarter = choose_quarter(matrix)

    try:
        chosen_item = choose_item(chosen_quarter)
        chosen_item.mark()
    except IndexError:
        print('There is no such item!')


def unmark_item(matrix):
    chosen_quarter = choose_quarter(matrix)

    try:
        chosen_item = choose_item(chosen_quarter)
        chosen_item.unmark()
    except IndexError:
        print('There is no such item!')


def remove_item(matrix):
    chosen_quarter = choose_quarter(matrix)
    chosen_item_index = choose_item_index()

    try:
        chosen_quarter.remove_item(chosen_item_index)
    except IndexError:
        print('There is no such item!')
