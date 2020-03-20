def main():
    try:
        x, y, z = [float(coor) for coor in input('x, y, z = ').split(',') if bool(coor) == True]
        print( (x**2 + y**2 + z**2) ** (1/2) )
    except:
        print('Bad input !')


if __name__ == '__main__':
    main()
