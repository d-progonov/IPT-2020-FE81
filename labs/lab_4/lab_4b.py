import random as rand

beg = 0
end = 0
ammount = 0
data_set = list()

def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def creation():
    try:
        beg = int(input("Please, input the integer begin number of range for random: "))
        end = int(input("Please, input the integer end number of range for random: "))
        ammount = int(input("Please, input the integer amount of elements: "))

        for i in range(ammount):
            data_set.append(rand.randint(beg, end))

        print(data_set)

    except ValueError:
        print("Please enter the integer data.")
        exit_func()
        creation()

def changes():
    for el in data_set:
        if el == 0:
            data_set.remove(0)   
    
    I = rand.randint(0, (len(data_set)-1))
    m = data_set[I-1] + 2

    for i in data_set:
        if i % 2 == 0:
            print("After this element", i, "will be inserted:", m)
            data_set.insert((data_set.index(i) + 1), m)
            break
    
    print(data_set)


if __name__ == "__main__":
    creation()
    changes()
    
        