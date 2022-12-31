# hello_psg.py

import PySimpleGUI as sg
sg.theme('DarkGrey8')

layout = [[sg.Titlebar("test2")],[sg.Text("BIG BULLYYYYYY!!!!")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout, resizable=True )

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
