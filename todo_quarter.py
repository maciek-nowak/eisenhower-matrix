from datetime import datetime
from todo_item import TodoItem


class TodoQuarter:
    def __init__(self):
        self.todo_items = []

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


def main():
    quater = TodoQuarter()
    quater.add_item('kot', datetime(2017, 10, 8))
    quater.add_item('pies', datetime(2017, 1, 8))
    quater.add_item('chomik', datetime(2017, 9, 8))
    quater.add_item('ryś', datetime(2017, 4, 3))

    print(quater.todo_items)
    print(quater)


if __name__ == '__main__':
    main()
