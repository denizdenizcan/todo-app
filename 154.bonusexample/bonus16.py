import FreeSimpleGUI as sg       #sg olarak kısalttım

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")     #FilesBrowse bir buton ekler ama normal bir button değildir.Kendine has tanımlanmış bir özelliği vardır.Dosyaları seçmek için programlanmıştır.

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")   #FolderBrowse: Bir buton ekler. Butona tıklandığında bir klasör seçme penceresi açılır.

compress_button = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[[label1,input1,choose_button1],
                                        [label2, input2, choose_button2],
                                          [compress_button]])

window.read()
window.close()