from datetime import datetime
from todo_item import TodoItem


class TodoQuarter:
    def __init__(self):
        """
        Method creates an instance of the class

        Returns:
            None
        """

        self.todo_items = []

    @property
    def height(self):
        return self.calculate_quarter_size()[0]

    @property
    def width(self):
        return self.calculate_quarter_size()[1]

    def sort_items(self):
        """
        Method sorts list in todo_items attribute by deadline in ascending direction

        Method changes object todo_items attribute

        Returns:
            None
        """

        self.todo_items.sort(key=lambda x: x.deadline)

    def add_item(self, title, deadline):
        """
        Method adds new object of TodoItem class into todo_items attribute list

        Args:
            title (str): name of the item
            deadline (obj): object of datetime class

        Returns:
            None
        """

        if type(deadline) is not datetime:
            raise TypeError

        self.todo_items.append(TodoItem(title, deadline))
        self.sort_items()

    def remove_item(self, index):
        """
        Method removes object of TodoItem class from todo_items attribute list

        Args:
            index (int): index of todo_items list

        Returns:
            None
        """

        self.todo_items.pop(index)

    def archive_items(self):
        """
        Method removes all objects with attribute is_done equal True from todo_items attribute list

        Args:
            index (int): index of todo_items list

        Returns:
            None
        """

        self.todo_items = [item for item in self.todo_items if not item.is_done]

    def get_item(self, index):
        """
        Method chooses proper object from todo_items attribute list

        Args:
            index (int): index of todo_items list

        Returns:
            (obj): object with proper index from todo_items attribute list
        """

        return self.todo_items[index]

    def __str__(self):
        """
        Method overloads the str operator

        Returns:
            listed_items (str): string used by print function
        """

        listed_items = [item.__str__() for item in self.todo_items]
        listed_items = [str(i+1) + '. ' + listed_items[i] for i in range(len(listed_items))]
        listed_items = '\n'.join(listed_items) + '\n'
        return listed_items

    def color__str__(self):
        """
        Method creates colored string with listed all objects from todo_items attribute list

        Returns:
            listed_items (str): colored string with object status
        """

        listed_items = [item.color__str__() for item in self.todo_items]
        listed_items = [str(i+1) + '. ' + listed_items[i] for i in range(len(listed_items))]
        listed_items = '\n'.join(listed_items) + '\n'
        return listed_items

    def calculate_quarter_size(self):
        """
        Method calculates quarters width and height

        Returns:
            width (int): quarters width
            height (int): quarters height
        """

        margin = 1
        quarter_text_list = self.__str__().splitlines()
        quarter_text_list = [line.strip() for line in quarter_text_list]
        height = len(quarter_text_list)
        width = len(max(quarter_text_list, key=len)) + 2 * margin
        return height, width


def main():
    quarter = TodoQuarter()
    quarter.add_item('kot', datetime(2017, 10, 8))
    quarter.add_item('pies', datetime(2017, 1, 8))
    quarter.add_item('chomik', datetime(2017, 9, 8))
    quarter.add_item('ryś', datetime(2017, 4, 3))

    print(quarter.todo_items)
    print(quarter)

    print(quarter.height, quarter.width)


if __name__ == '__main__':
    main()
