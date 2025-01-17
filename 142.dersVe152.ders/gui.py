import functions
import FreeSimpleGUI


label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo")
add_button = FreeSimpleGUI.Button("Add")


window = FreeSimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()

# Window içine pencerenin aldığı değerleri ekleriz.
#layout her zaman liste bekler.Layout da iç köşeli parantezin içine koyduğumuz ögeler bir satıra yerleştirilir.
#eğer layout içine yazdıkların ayrı ayrı satırlarda gözüksün istiyorsan her birini köşeli paranteze al.