import module1 as md
import PySimpleGUI as sg

answer = ''

while (True):
    while(answer.count('\n')>=20):
        answer = answer[answer.find('\n')+1:]

    sg.ChangeLookAndFeel('GreenTan')

    window = sg.Window('Object Menu', default_element_size=(40, 1), size = (600,550))

    sg.Spin(('new','del','set location','get location'))
    layout = [
       [sg.Radio('TLocation',"group", size=(7,1), default = True), sg.Text(size=(3,1), text=str(len(md.TLocation.instances))), sg.Spin(values=(md.TLocation.instances), size=(47,1)), sg.Spin(size=(10,1),values=('new','delete','set location','get location'))],
       [sg.Radio('TPoint',"group", size=(7,1)), sg.Text(size=(3,1), text=str(len(md.TPoint.instances))+'/'+str(md.TPoint.limit)), sg.Spin(values=(md.TPoint.instances), size=(47,1)), sg.Spin(size=(10,1),values=('new','delete','set location','get location','move','set colour','get colour'))],
       [sg.Radio('TEllipse',"group", size=(7,1)), sg.Text(size=(3,1), text=str(len(md.TEllipse.instances))+'/'+str(md.TEllipse.limit)), sg.Spin(values=(md.TEllipse.instances), size=(47,1)), sg.Spin(size=(10,1),values=('new','delete','set location','get location','move','set colour','get colour','set size','get size'))],
       [sg.Radio('TKrug',"group", size=(7,1)), sg.Text(size=(3,1), text=str(len(md.TKrug.instances))+'/'+str(md.TKrug.limit)), sg.Spin(values=(md.TKrug.instances), size=(47,1)), sg.Spin(size=(10,1),values=('new','delete','set location','get location','move','set colour','get colour','set size','get size','set radius','get radius'))],
       [sg.Radio('TPie',"group", size=(7,1)), sg.Text(size=(3,1), text=str(len(md.TPie.instances))+'/'+str(md.TPie.limit)), sg.Spin(values=(md.TPie.instances), size=(47,1)), sg.Spin(size=(10,1),values=('new','delete','set location','get location','move','set colour','get colour','set size','get size','set radius','get radius','set degrees','get degrees'))],
       [sg.Text(size=(72, 20),text=answer,background_color='#d3dfda')],
       [sg.Submit(size=(16,2)), sg.Column([[sg.InputText(size=(12,1),default_text='move x, set x')], [sg.InputText(size=(12,1),default_text='move y, set y')]]), sg.Column([[sg.InputText(size=(12,1),default_text='set width')], [sg.InputText(size=(12,1),default_text='set hight')]]), sg.Column([[sg.InputText(size=(12,1),default_text='start degree')], [sg.InputText(size=(12,1),default_text='extent degree')]]), sg.Column([[sg.InputText(size=(12,1),default_text='set radius')], [sg.InputText(size=(12,1),default_text='colour, colour')]])]
    ]
    event, values = window.Layout(layout).Read()
    window.close()
    if event in (None, 'Exit'):
        break

    if values[0]==1:
        c = md.TLocation
        cname = 'TLocation'
        do = values[2]
        obj = values[1]
    elif values[3]==1:
        c = md.TPoint
        cname = 'TPoint'
        do = values[5]
        obj = values[4]
    elif values[6]==1:
        c = md.TEllipse
        cname = 'TEllipse'
        do = values[8]
        obj = values[7]
    elif values[9]==1:
        c = md.TKrug
        cname = 'TKrug'
        do = values[11]
        obj = values[10]
    elif values[12]==1:
        c = md.TPie
        cname = 'TPie'
        do = values[14]
        obj = values[13]
    else:
        c = None
    if not c == None:
        if do == 'new':
            if c == md.TLocation:
                instance = c(values[15], values[16])
            elif c == md.TPoint:
                instance = c(values[15], values[16], values[22])
            elif c == md.TKrug:
                instance = c(values[15], values[16], values[22], values[21])
            elif c == md.TPie:
                instance = c(values[15], values[16], values[22], values[21], values[19], values[20])
            elif c == md.TEllipse:
                instance = c(values[15], values[16], values[22], values[17], values[18])
            answer += '>>'+str(instance)[9:-1]+'\n'
            if instance == None:
                answer += 'Reached limit for objects of class {}.\n'.format(cname)
            else:
                answer += 'Created new object of class {}.\n'.format(cname)
        else:
            answer += '>>'+str(obj)[9:-1]+'\n'
        if do == 'delete' and type(obj)==c:
            c.instances[c.instances.index(obj)].__del__()
            answer += 'Deleted selected object of class {}.\n'.format(cname)
        elif do == 'set location' and type(obj)==c:
            answer += 'Setting selected object of {} class on: x = {}, y = {}.\n'.format(cname, values[15], values[16])
            obj.set_location(values[15], values[16])
            coordinates = obj.get_location()
            answer += 'Object is now located on: x = {}, y = {}.\n'.format(coordinates[0], coordinates[1])
        elif do == 'get location' and type(obj)==c:
            coordinates = obj.get_location()
            answer += 'Selected object of {} class is located on: x = {}, y = {}.\n'.format(cname, coordinates[0], coordinates[1])
        elif do == 'set colour' and type(obj)==c:
            if cname == 'TEllipse':
                answer += 'Changing colours of selected object of {} class to: {}.\n'.format(cname, values[22])
                temp = values[22].split(', ')
                obj.set_colour(temp)
                coordinates = obj.get_colour()
                answer += 'Colours of the selected object are now: {}, {}.\n'.format(coordinates[0], coordinates[1])
            else:
                answer += 'Changing colour of selected object of {} class to: {}.\n'.format(cname, values[22])
                obj.set_colour(values[22])
                answer += 'Colour of the selected object is now: {}.\n'.format(obj.get_colour())
        elif do == 'get colour' and type(obj)==c:
            if cname == 'TEllipse':
                coordinates = obj.get_colour()
                answer += 'Colours of the selected object of {} class are: {}, {}.\n'.format(cname, coordinates[0], coordinates[1])
            else:
                answer += 'Colour of the selected object of {} class is: {}.\n'.format(cname, obj.get_colour())
        elif do == 'move' and type(obj)==c:
            answer += 'Moving selected object of {} class to: x = {}, y = {}.\n'.format(cname, values[15], values[16])
            obj.move(values[15], values[16])
            coordinates = obj.get_location()
            answer += 'Object is now located on: x = {}, y = {}.\n'.format(coordinates[0], coordinates[1])
        elif do == 'set size' and type(obj)==c:
            answer += 'Setting size of selected object of {} class to: width = {}, hight = {}.\n'.format(cname, values[17], values[18])
            obj.set_size(values[17], values[18])
            coordinates = obj.get_size()
            answer += 'Size of selected object is now: width = {}, hight = {}.\n'.format(coordinates[0], coordinates[1])
        elif do == 'get size' and type(obj)==c:
            coordinates = obj.get_size()
            answer += 'Size of selected object of {} class is: width = {}, hight = {}.\n'.format(cname, coordinates[0], coordinates[1])
        elif do == 'set radius' and type(obj)==c:
            answer += 'Setting radius of selected object of {} class to: {}.\n'.format(cname, values[21])
            obj.set_radius(values[21])
            answer += 'Radius of the selected object is now: {}\n'.format(obj.get_radius())
        elif do == 'get radius' and type(obj)==c:
            answer += 'Radius of the selected object of {} class is: {}\n'.format(cname, obj.get_radius())
        elif do == 'set degrees' and type(obj)==c:
            answer += 'Setting start degree and extent degree of selected object of {} class to: {} and {}.\n'.format(cname, values[19], values[20])
            obj.set_degrees(values[19], values[20])
            coordinates = obj.get_degrees()
            answer += 'Start degree and extent degree of selected object are now: start degree = {}, extent = {}.\n'.format(coordinates[0], coordinates[1])
        elif do == 'get degrees' and type(obj)==c:
            coordinates = obj.get_degrees()
            answer += 'Start degree and exnent degree of selected object are: start degree = {}, extent = {}.\n'.format(coordinates[0], coordinates[1])
        else:
            if do != 'new' and type(obj)==c:
                answer += 'Wrong syntax: there is no method _{}_ for class {}.\n'.format(do, cname)
            elif do != 'new' and type(obj)!=c:
                answer += 'Did you forget to create an object of {} class?\n'.format(cname)
print('Press Enter to exit...')