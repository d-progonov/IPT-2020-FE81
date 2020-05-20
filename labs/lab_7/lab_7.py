def in_data():
    string_1 = input("Please enter a text line for searching:\n")
    string_2 = input("\nPlease enter a text line,\nfrom which you will be searching an element positions: \n")
    print("\nChoose an element you want to search in 2-nd line. \nLast element you can choose is ", len(string_2), ".")
    sym = int(input())

    return string_1, string_2, sym

def count(string_1, string_2, sym):
    counter = 0
    data = list()
    k = string_2[sym - 1]
    for i in string_1:
        counter += 1
        if i == k:
            data.append(counter)
    if len(data) == 0:
        print("\n-1. This element hasn't been meeted.")
        return -1
    else:
        print("\nThis element has been meeted in next positions:")
        for i in data:
            print(str(i))
        return data

def main():
    a, b, c = in_data()
    count(a, b, c)
    

if __name__ == "__main__":
    main()
