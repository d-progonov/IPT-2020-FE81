class PhoneNumber:
    def __init__(self, name, number, mail):
        self.name = name
        self.number = number
        self.mail = mail

    def display_info(self):
        print("Name: ", self.name)
        print("Number: ", self.number)
        print("Mail: ", self.mail)
