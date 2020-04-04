def get_data():
    try:
        return open('input').readline()
    except:
        print('Something wrong with input file')
        exit()
