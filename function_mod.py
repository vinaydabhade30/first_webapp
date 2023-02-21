FILEPATH = 'todolist-ifelifelse.txt'


def file_open_r(filename=FILEPATH):
    """ function for open txt file and read todolist"""
    with open(filename, 'r') as file_r:
        todo_r = file_r.readlines()
    return todo_r


def file_open_w(get_att, filename=FILEPATH):
    """function for open file and write and update todolist"""
    with open(filename, 'w') as file_w:
        file_w.writelines(get_att)
        return


if __name__ == "__main__":
    print("this line import from function mod")
