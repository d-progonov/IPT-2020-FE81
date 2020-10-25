from l10_classes import PhoneNumber

def new_contact(i):
    try:
        print("If you don't enter a parameter, it will be saved as \"None\"")
        nm = input("Please, print the name of this contact: ")
        num = input("Please, print the number of this contact: ")
        mail = input("Please, print the mail of this contact: ")
        for i in num:
            if i.isdigit() or (num.index("+") == 0):
                continue
        res = PhoneNumber(nm, num, mail)
        return res
    
    except ValueError:
        print("You have to enter a phone number only with digits\n(you can also begin a phone number with \"+\")\n")
        new_contact(i)

def search_contact(book):
    print("If you don't want to input key, just press \"Enter\"")

    key_name = input("Enter a name key: ") 
    key_num = input("Enter a number key: ")
    key_mail = input("Enter a name key: ")

    print("Results of search:\n----------")
    for i in book:
        if (key_name in i.name) and (key_num in i.number) and (key_mail in i.mail):
            i.display_info()
            print("----------")



def menu(contact_book, i = 0):
    print("\nPlease, choose your action:\n")
    print("Press \"a\" if you want to add a contact.")
    print("Press \"f\" if you want to find a contact.")
    print("Press \"s\" if you want to see all phonebook")
    print("Press \"e\" to end this session.")

    ans = str(input("Your answer: ")).lower()
    print("\n")

    if ans == "a":
        contact_book.append(new_contact(i))
        menu(contact_book, i)
        print("Contact was added.")
    elif ans == "f":
        search_contact(contact_book)
        menu(contact_book, i)
    elif ans == "s":
        print("\n----PhoneBook----\n")
        for i in contact_book:
            k = i
            k.display_info()
            print("------------------")
        menu(contact_book, i)
    elif ans == "e":
        raise SystemExit(0)
    else:
        print("You have to choose your action.")
        menu(contact_book, i)
        
