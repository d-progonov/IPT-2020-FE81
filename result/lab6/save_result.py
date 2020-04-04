def save_result(result):
    try:
        open('output','w').write(result)
    except:
        print('Something wrong with output file')
        exit()
