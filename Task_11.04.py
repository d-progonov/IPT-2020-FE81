import PySimpleGUI as sg

answer = ''
work_started = False
while (True):
    if answer.count('\n')>=20:
        answer = answer[answer.find('\n')+1:]

    sg.ChangeLookAndFeel('GreenTan')

    window = sg.Window('Task')

    layout = [
       [sg.Button('Start'), sg.Button('Check'), sg.Button('Finish')],
       [sg.Text(size=(20,1), text=answer)]
    ]
    event = window.Layout(layout).Read()
    window.close()
    if event == (None, {}):
        break
    if event == ('Start', {}):
        work_started = True
    elif event == ('Check', {}):
        if work_started == True:
            answer = "Work is in progress"
        else:
            answer = "No work here"
    elif event == ('Finish', {}):
        work_started = False
