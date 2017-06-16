from datetime import datetime


class TodoItem:
    def __init__(self, title, deadline):
        if type(title) is not str or type(deadline) is not datetime:
            raise TypeError

        self.title = title
        self.deadline = deadline
        self.is_done = False

    def mark(self):
        self.is_done = True

    def unmark(self):
        self.is_done = False

    def __str__(self):
        mark = {True: '[x] ', False: '[ ] '}
        item_status = mark[self.is_done] + str(self.deadline.day) + '-' + str(self.deadline.month) + ' ' + self.title
        return item_status

    def color__str__(self):
        RESET_COLOR = '\033[0m'
        RED = '\033[31m'
        ORANGE = '\033[33m'
        GREEN = '\033[32m'

        time_to_deadline = (self.deadline - datetime.today()).days
        if time_to_deadline < 0:
            color = RED
        elif time_to_deadline < 3:
            color = ORANGE
        else:
            color = GREEN

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
