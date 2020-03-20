try:
    print("Enter XYZ coordinates your vector ")
    x = float(input("x="))
    y = float(input("y="))
    z = float(input("z="))
    module = (x**2+y**2+z**2)**(1/2)
    print("module your vector=", module)
except ValueError:
    print("ERROR!!! you should enter a number but not string!!!")