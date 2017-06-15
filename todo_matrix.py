from datetime import datetime
import common
from todo_quarter import TodoQuarter


class TodoMatrix:
    def __init__(self):
        self.todo_quarters = {
            'IU': TodoQuarter(),
            'IN': TodoQuarter(),
            'NU': TodoQuarter(),
            'NN': TodoQuarter()}

    def get_quarter(self, status):
        chosen_quarter = self.todo_quarters[status]
        return chosen_quarter

    def add_item(self, title, deadline, is_important=False):
        if type(deadline) is not datetime:
            raise TypeError
        quarter_name = common.choose_quarter_name(deadline, is_important)
        self.todo_quarters[quarter_name].add_item(title, deadline)

    def add_items_from_file(self, file_name):
        item_list = common.read_file(file_name)
        item_list = common.prepare_items_to_add(item_list)

        for item in item_list:
            self.add_item(item[0], item[1], item[2])

    def save_items_to_file(self, file_name):
        list_to_save = common.create_list_to_save(self)

        list_to_save = common.prepare_items_to_save(list_to_save)

        with open(file_name, 'w') as datafile:
            datafile.writelines(list_to_save)

    def archive_items(self):
        for key in self.todo_quarters:
            self.todo_quarters[key].todo_items = [
                item for item in self.todo_quarters[key].todo_items if not item.is_done]

    def __str__(self):
        listed_quaters = [key + '\n' + self.get_quarter(key).__str__() for key in self.todo_quarters]
        listed_quaters = '\n'.join(listed_quaters)
        return listed_quaters


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
    # print('IU', matrix.todo_quarters['IU'])
    # print('IN', matrix.todo_quarters['IN'])
    # print('NU', matrix.todo_quarters['NU'])
    # print('NN', matrix.todo_quarters['NN'])
    print(matrix)
    matrix.save_items_to_file('todo_items.csv')


if __name__ == '__main__':
    main()
