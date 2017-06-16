from datetime import datetime
import common


class TodoItem:
    def __init__(self, title, deadline):
        """
        Method creates an instance of the class

        Args:
            title (str): name of the item
            deadline (obj): object of datetime class

        Returns:
            None
        """

        if type(title) is not str or type(deadline) is not datetime:
            raise TypeError

        self.title = title
        self.deadline = deadline
        self.is_done = False

    def mark(self):
        """
        Method changes value of object is_done attribute to True

        Returns:
            None
        """

        self.is_done = True

    def unmark(self):
        """
        Method changes value of object is_done attribute to False

        Returns:
            None
        """

        self.is_done = False

    def __str__(self):
        """
        Method overloads the str operator

        Returns:
            item_status (str): string used by print function
        """

        mark = {True: '[x] ', False: '[ ] '}
        item_status = mark[self.is_done] + str(self.deadline.day) + '-' + str(self.deadline.month) + ' ' + self.title
        return item_status

    def color__str__(self):
        """
        Method creates colored string with object status

        Returns:
            item_status (str): colored string with object status
        """

        RESET_COLOR = '\033[0m'
        color = common.choose_item_color(self.deadline)

        mark = {True: '[x] ', False: '[ ] '}
        item_status = color + mark[self.is_done] + str(self.deadline.day) + '-' + str(
            self.deadline.month) + ' ' + self.title + RESET_COLOR

        return item_status


def main():
    a = TodoItem('kot', datetime(2017, 4, 8))

    a.mark()
    print(a)


if __name__ == '__main__':
    main()
