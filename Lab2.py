while(True):
    print("1.Want to say hello?\n2.Ready to work?\n3.Are you tired?\n ")
    try:
        a = int(input())
        if a == 1:
            print("Hello :D\n")
        elif a == 2:
            print("Let's work on the computer!!!\n")
        elif a == 3:
            print("Good bye...Computer shuts down\n")
            exit()
        else:
            print("Chose something from menu")
    except ValueError:
        print("Wrong data type")
