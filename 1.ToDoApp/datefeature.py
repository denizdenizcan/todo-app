import functions  #functions modülünü biz burada kendimiz oluşturduk.O yüzden yerel bir modüldür.Yani yerel proje dizinimizde bulunur.
import time   #bu modül Python geliştiricileri tarafından oluşturuldu.Yani standart bir modüldür.Burda dizin içinde bir dosya oluşturulmaz.Yani python un kendi kurulum dizininde bulunur.

now = time.strftime("%b %d, %Y  %H:%M:%S")   #çalıştırdığın zamanki tarih ve saati ekrana yazdırır.
print("It is", now)                   # b=ay, d=gün, Y=year H=saat M=dakika S=Saniye


while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()   #functions modülüne girer ve get_todos u çağırır.

        todos.append(todo + '\n')

        functions.write_todos(todos)      #functions modülüne girer ve write_todos u çağırır.

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # bu satırda item ögesinden \n çıkarmış olduk.
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo:")  # list içinde değişiklik yapmak istedik.
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:  # eğer kullancıcı edit in yanına rakam değilde todo girerse program hata üretmesin diye except bloğu içine aldık.ve kullanıcıya mesaj verdik.
            print("Your command is not valid")
            continue  # continue aşağıdaki kodların hepsini yok sayar,en yukarı çıkar ve 2.satırdan başlar ve çalıştırır.


    elif user_action.startswith( 'complete'):
        try:
            number = int(user_action[9:])  # IndexError hatası veriyor list index out of range

            todos = functions.get_todos()

            todo_to_remove = todos[number - 1].strip('\n')  # todo_to_remove değişkeninden '\n' ifadeyi çıkardık.

            todos.pop(number - 1)  # list.pop(index)  söz konusu indexe sahip öge kaldırılır.Todos tekrar güncellenmiş olur.

            functions.write_todos(todos)


            message = f"Todo {todo_to_remove} was removed from the list."  # Hangi ögenin kaldırıldığını mesaaj ile kullancıya göstermek istedim.
            print(message)
        except IndexError:
            print("There is no item with that number")  # bu numaraya sahip bir öge yok demek istedim.
            continue  # kullanıcının tekrar yeni komut girmesine izin vermiş olduk.

    elif user_action.startswith('exit'):
        break
    else:  # koşullardan hiçbiri doğru değilse kullanıcıya mesaj verebilmek için else kullandık.
        print("Command is not valid.")
