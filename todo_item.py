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


def main():
    a = TodoItem('kot', datetime(2017, 4, 8))

    a.mark()
    print(a)


if __name__ == '__main__':
    main()
