def read_file():
    with open('todos.txt', 'r') as file:
        local_todos = file.readlines()
        return local_todos


def write_file(todos):
    with open('todos.txt', 'w') as file:
        for todo in todos:
            file.writelines(todo)