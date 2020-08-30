import PySimpleGUI as sg

layout = [[sg.Text('My one-shot window.', key='-out-')],
          [sg.InputText(key='-out2-')],
          [sg.Submit()]]

window = sg.Window('Window Title', layout)

while True:

    event, values = window.read()
    print(event)
    if event == "Submit":
        vs = values['-out2-']
        window['-out-'].update(vs)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
sg.popup('You entered', vs)