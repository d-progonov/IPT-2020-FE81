import math

def main():
    try:
        x = input('x = ')
        y = input('y = ')
        x, y = float(x), float(y)
        print('Result: ', pow((1 - math.tan(x)), (math.cos(x)/math.sin(x))) + math.cos(x - y) )
    except ZeroDivisionError:
        print('Division by zero !')
    except:
        print('Bad input !')

if __name__ == '__main__':
    main()
