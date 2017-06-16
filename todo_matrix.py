from datetime import datetime
import common
from todo_quarter import TodoQuarter


class TodoMatrix:
    def __init__(self):
        """
        Method creates an instance of the class

        Returns:
            None
        """

        self.todo_quarters = {
            'IU': TodoQuarter(),
            'IN': TodoQuarter(),
            'NU': TodoQuarter(),
            'NN': TodoQuarter()}

    def get_quarter(self, status):
        """
        Method chooses proper object from todo_quarters attribute dictionary

        Args:
            status (str): quarter name

        Returns:
            (obj): object with proper name from todo_quarters attribute dictionary
        """
        chosen_quarter = self.todo_quarters[status]
        return chosen_quarter

    def add_item(self, title, deadline, is_important=False):
        """
        Method adds new object of TodoQuarter class into todo_quarters attribute dictionary

        Args:
            title (str): name of the item
            deadline (obj): object of datetime class
            is_important (bool): True if item is important

        Returns:
            None
        """

        if type(deadline) is not datetime:
            raise TypeError
        quarter_name = common.choose_quarter_name(deadline, is_important)
        self.todo_quarters[quarter_name].add_item(title, deadline)

    def add_items_from_file(self, file_name):
        """
        Method adds from file new objects of TodoItem class into todo_items attribute lists of quarters

        Args:
            file_name (str): name of the file

        Returns:
            None
        """

        item_list = common.read_file(file_name)
        item_list = common.prepare_items_to_add(item_list)

        for item in item_list:
            self.add_item(item[0], item[1], item[2])

    def save_items_to_file(self, file_name):
        """
        Method saves to the file all objects of TodoItem class

        Args:
            file_name (str): name of the file

        Returns:
            None
        """

        list_to_save = common.create_list_to_save(self)

        list_to_save = common.prepare_items_to_save(list_to_save)

        with open(file_name, 'w') as datafile:
            datafile.writelines(list_to_save)

    def archive_items(self):
        """
        Method removes all objects with is_done attribute from todo_items attribute lists of quarters

        Returns:
            None
        """

        for key in self.todo_quarters:
            self.todo_quarters[key].todo_items = [
                item for item in self.todo_quarters[key].todo_items if not item.is_done]

    @property
    def columns_width(self):
        quarters_widths = [self.get_quarter(key).width for key in self.todo_quarters]

        columns_width = max(quarters_widths + [len(' urgent '), len(' not urgent ')])

        return columns_width

    @property
    def rows_height(self):
        quarters_heights = [self.get_quarter(key).height for key in self.todo_quarters]

        rows_height = max(quarters_heights + [len('important'), len('not important')])

        return rows_height

    def __str__(self):
        """
        Method overloads the str operator

        Returns:
            listed_items (str): string used by print function
        """

        titles_row = common.prepare_titles_row(self.columns_width)
        border_row = common.prepare_border_row(self.columns_width)

        important_rows = common.prepare_important_rows(
            [self.get_quarter(status).color__str__() for status in ['IU', 'IN']],
            self.columns_width, self.rows_height, 'IMPORTANT')

        not_important_rows = common.prepare_important_rows(
            [self.get_quarter(status).color__str__() for status in ['NU', 'NN']],
            self.columns_width, self.rows_height, 'NOT IMPORTANT')

        matrix_to_print = '\n'.join(
            [titles_row, border_row, important_rows, border_row,  not_important_rows, border_row])
        return '\n' + matrix_to_print + '\n'


def main():
    matrix = TodoMatrix()
    matrix.add_item('kot', datetime(2017, 10, 8))
    matrix.add_item('pies', datetime(2017, 1, 8))
    matrix.add_item('chomik', datetime(2017, 9, 8))
    matrix.add_item('ryś', datetime(2017, 4, 3), True)
    matrix.add_item('ryśd', datetime(2017, 7, 3), True)
    matrix.get_quarter('IN').get_item(0).mark()
    matrix.add_items_from_file('todo_items_read_test.csv')
    matrix.archive_items()
    print(matrix)
    matrix.save_items_to_file('todo_items.csv')
    print(matrix.columns_width, matrix.rows_height)


if __name__ == '__main__':
    main()
