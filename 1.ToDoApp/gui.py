import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # to-do bu giriş kutusunun kimlğidir.
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))           #mevcut yapılcakların listesini verir.
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                          [label],
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                          [exit_button]],
                   font=('Helvetica', 20))          # font yazı tipi ve büuüklüğünü ayarlar.

while True:
    event, values = window.read(timeout=200)  # window.read metodu bir tuple döndürür.event values iki ögeli tuple olarak döndürür.
    window["clock"].update(value=time.strftime("%b,%d,%Y %H:%M:%S"))
                                           # Bir buttona basmak bir olaydır.ve event basılan button un etiketini alır.
                                             # values değişkeni kullanıcı tarafından doldurulan değerleri alır.
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)   #edit ettiğin todos hemen listbox içinde güncel görünmesi için update function kullandık.
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))   #kullanıcıya popup ile bilgi,uyarı mesajı verebilirsin.
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first,", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

# Window içine pencerenin aldığı değerleri ekleriz.
# layout her zaman liste bekler.Layout da iç köşeli parantezin içine koyduğumuz ögeler bir satıra yerleştirilir.
# eğer layout içine yazdıkların ayrı ayrı satırlarda gözüksün istiyorsan her birini köşeli paranteze al.
# input_box ve add_button aynı köşeli parantezin içinde olduğundan aynı satırda yazılmış oldu.
"""
window.read() yöntemi, PySimpleGUI kütüphanesinde bir pencerenin olaylarını ve girdilerini yakalamak için kullanılır. Bu yöntem bir tuple (demet) döndürür ve iki öğe içerir:

Event (Olay): Kullanıcının yaptığı eylemi temsil eder. Örneğin, bir düğmeye tıklama, bir menüden seçim yapma, pencereyi kapatma gibi.
Values (Değerler): Pencerede bulunan tüm giriş elemanlarının (ör. metin kutuları, onay kutuları) mevcut değerlerini içeren bir sözlük.
"""

"""
Çıktı
Olay (event):
Kullanıcı "Tamam" düğmesine tıklarsa, event "Tamam" döner.
Kullanıcı pencereyi kapatırsa, event sg.WINDOW_CLOSED döner.

Değerler (values):
{"input": "kullanıcı girişi"} gibi bir sözlük döner. Anahtarlar, elemanların key değerleridir.

Genel Kullanım
Olay kontrolü için: Hangi düğmeye basıldığını ya da pencerenin kapanıp kapanmadığını belirler.
Kullanıcı girdilerini almak için: Değerler sözlüğünden erişilir.
"""
#35. satır ListBox'ı günceller, 37. satır ise düzenlenmek üzere seçilen görevi metin kutusuna aktarır.