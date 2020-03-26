text = str(input("Input some text using Cyrillic alphabet:"))

message = list(text)
coded = list(text)
decoded = list(text)

alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

while True:
    try:
        differ = int(input("Input the number of symbols to be moved:"))
        if differ == 0:
            print("Nothing will change with '0' step of movement. Please, choose another value:")
            continue
        elif differ < 0:
            print("Please input positive number to get correct answer!")
            continue
        break
    except ValueError:
        print("Invalid value entered!")

shift = differ % len(alphabet)


def coding():
    for i in range(len(message)):
        if not message[i].lower() in alphabet:
            coded[i] = message[i]
            continue
        
        position = alphabet.index(message[i].lower())
        index = 0
