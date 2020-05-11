from nltk.tokenize import RegexpTokenizer

path = 'words.txt'
dictionary = open(path).read()

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(dictionary)

n = 0
j = 0
help = []
sorry = 'Unfortunately, I have nothing for you :( '
word = input('Enter the beginning of a word: ')

for i in words:
        while (j < len(word) and j < len(i)):
                if i[j] == word[j]:
                    n += 1
                    if (n == len(word)):
                        help.append(i)
                        break
                else:
                    break
                j += 1

        if len(help) < 3:
            j = 0
            n = 0
        else: 
            break

        if i == "zeropoint":
            if len(help) == 0:
                help = sorry
                break
            else:
                break

print (help)
help = []

ans = input('Another word? Please answer yes or no: ')

while ans != 'no':
    if ans == 'yes':
        word = input('Enter the beginning of a word: ')

        for i in words:
            while (j < len(word) and j < len(i)):
                if i[j] == word[j]:
                    n += 1
                    if (n == len(word)):
                        help.append(i)
                        break
                else:
                    break
                j += 1

            if len(help) < 3:
                j = 0
                n = 0

            else:
                break

            if i == "zeropoint":
                if len(help) == 0:
                    help = sorry
                    break
                else:
                    break

        print (help)
        help = []
        ans = input('Another word? Please answer yes or no: ')

    else:
        ans = input('Please answer yes or no: ')

print('Have a good day! :)')

