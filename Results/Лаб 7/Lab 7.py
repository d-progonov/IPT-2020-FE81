text = str(input("ВВедите символы для шифровки:"))

my_list = list(text)

count_zero = my_list.count('0')

count_one = my_list.count('1')

plus = count_zero + count_one

new_list = [None] * plus

transformed = [None] * len(new_list)

decoded = [None] * len(new_list)



def sorting():

    k = 0

    for i in range(len(my_list)):

        if my_list[i] == '0':

            new_list[k] = my_list[i]

            k += 1

        if my_list[i] == '1':

            new_list[k] = my_list[i]

            k += 1

    print("Исходное шифрование:", new_list)

    

def coding():

    for i in range(1, len(new_list)):

        transformed[0] = new_list[0]

        if new_list[i] == new_list[i - 1]:

            transformed[i] = '1'

        else:

            transformed[i] = '0'

    print("Зашифрованые символы:", transformed)



def decoding():

    for i in range(1, len(transformed)):

        decoded[0] = transformed[0]

        if transformed[i] == '1':

            decoded[i] = decoded[i - 1]

        elif transformed[i] == '0':

            if decoded[i - 1] == '1':

                decoded[i] = '0'

            else:

                decoded[i] = '1'

    print("Разшифрованые символы:", decoded)



if __name__ == '__main__':



    sorting()

    coding()

    decoding()
