def r():
    with open ('todos.txt','r') as file:
        file_local = file.readlines()
    return file_local

def w(todos):
    with open ('todos.txt', 'w') as file:
        file1 = file.writelines(todos)
    return file1

