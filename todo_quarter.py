from datetime import datetime
from todo_item import TodoItem


class TodoQuarter:
    def __init__(self):
        self.todo_items = []

    @property
    def height(self):
        return self.calculate_quarter_size()[0]

    @property
    def width(self):
        return self.calculate_quarter_size()[1]

    def sort_items(self):
        self.todo_items.sort(key=lambda x: x.deadline)

    def add_item(self, title, deadline):
        if type(deadline) is not datetime:
            raise TypeError

        self.todo_items.append(TodoItem(title, deadline))
        self.sort_items()

    def remove_item(self, index):
        self.todo_items.pop(index)

    def archive_items(self):
        self.todo_items = [item for item in self.todo_items if not item.is_done]

    def get_item(self, index):
        return self.todo_items[index]

    def __str__(self):
        listed_items = [item.__str__() for item in self.todo_items]
        listed_items = [str(i+1) + '. ' + listed_items[i] for i in range(len(listed_items))]
        listed_items = '\n'.join(listed_items) + '\n'
        return listed_items

    def color__str__(self):
        listed_items = [item.color__str__() for item in self.todo_items]
        listed_items = [str(i+1) + '. ' + listed_items[i] for i in range(len(listed_items))]
        listed_items = '\n'.join(listed_items) + '\n'
        return listed_items

    def calculate_quarter_size(self):
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
