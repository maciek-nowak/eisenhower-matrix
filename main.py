import os
from datetime import datetime
from todo_item import TodoItem
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix
import main_logic


def handle_menu():
    """
    Function prints main menu

    Returns:
        None
    """

    options = """Choose your option:
                1. Add new item
                2. Mark item as done
                3. Mark item as undone
                4. Remove chosen item
                5. Remove all done items
                6. Save items to the file
                0. Remove all done items, save items to the file and quit\n"""

    print(options)


def choose_and_start_option(matrix):
    """
    Function gets input from user and runs proper function

    Args:
        matrix (obj): object represents whole Eisenhower Matrix

    Returns:
        exit (bool): if True exits the aplication
    """

    exit = False

    user_option = input("Please choose an option number: ")
    if user_option == "1":
        main_logic.add_item(matrix)
    elif user_option == "2":
        main_logic.mark_item(matrix)
    elif user_option == "3":
        main_logic.unmark_item(matrix)
    elif user_option == "4":
        main_logic.remove_item(matrix)
    elif user_option == "5":
        matrix.archive_items()
    elif user_option == "6":
        matrix.save_items_to_file('todo_items.csv')
    elif user_option == "0":
        matrix.archive_items()
        matrix.save_items_to_file('todo_items.csv')
        exit = True
    else:
        print("There is no such option.")

    return exit


def main():
    os.system('clear')
    print('Welcome to Eisenhower Matrix!\n')
    matrix = TodoMatrix()

    try:
        matrix.add_items_from_file('todo_items.csv')
    except FileNotFoundError:
        print('Database file not found! No items were imported')

    exit = False
    while not exit:
        print(matrix)
        handle_menu()
        exit = choose_and_start_option(matrix)

    print('Thank you for using Eisenhower Matrix. See you next time!')


if __name__ == '__main__':
    main()
