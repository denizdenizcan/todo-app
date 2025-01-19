import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="to-do")  # to-do bu giriş kutusunun kimlğidir.
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))  # font yazı tipi ve büuüklüğünü ayarlar.

while True:
    event, values = window.read()  # window.read metodu bir tuple döndürür.event values iki ögeli tuple olarak döndürür.
    print(event)  # Bir buttona basmak bir olaydır.ve event basılan button un etiketini alır.
    print(values)  # values değişkeni kullanıcı tarafından doldurulan değerleri alır.
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
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
