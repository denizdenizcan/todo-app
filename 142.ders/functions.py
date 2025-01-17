FILEPATH = "todos.txt"
#genellikle büyük harflerle yazılır.Sabit değerimi tutmak için bir değişkene eşitledim.Böylece
#textfile adını değiştirmek istersem direkt burdan değiştirebilirim.


def get_todos(filepath=FILEPATH):     # filepath ı default parametre olarak ekledim.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):    #burda iki tane parametre girdim.filepath default parametre, todos_arg ise default değildir.Ama aynı satırda default ve default olmayanı yazabilmen için ilk önce default olmayanı yazman gerekir.
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


