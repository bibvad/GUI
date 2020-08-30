import PySimpleGUI as sg

layout = [[sg.Text('My one-shot window.', key='-out-')],
          [sg.InputText()],
          (sg.Submit(), sg.Cancel())]

window = sg.Window('Window Title', layout)

while True:

    event, values = window.read()
    print(event)
    if event == "Submit":
        print(values)
        window['-out-'].update("Babsas")

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

text_input = values[0]
sg.popup('You entered', text_input)
