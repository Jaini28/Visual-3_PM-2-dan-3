import PySimpleGUI as sg

sg.theme_text_color('#292d32')
texts = [
    [sg.Text("NPM : 2210010042")],
    [sg.Text("Nama : Ahmad jaini")],
    [sg.Text("Kelas : TI O Reg Banjarmasin")],
    [sg.Text("Matkul : Visual 3")]
]

window = sg.Window(title='Latihan Pertama', layout=texts, size=(600, 300), font=('Georgia', 20))
window()
window.close()
