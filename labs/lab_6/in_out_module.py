def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def open_file():
    try:
        file_name = input("Please enter way to a condition file: ")
        data = []
        with open(file_name, "r") as f:
            for line in f:
                data.append([float(x) for x in line.split()])
        
        if data[0][2] == 0:
            raise Exception("Please, enter a number of element, bigger than 0")
        
        a = data[0][0]
        b = data[0][1]
        c = data[0][2]
        print("Data was readed")

        return a, b, c
    except FileNotFoundError:
        print("You have to enter a wrong way or the way to existing file.")
    
    except Exception as e:
        print("", e)
        
        

def write_file(data):
    with open("res.txt", "w") as f:
        f.write("Geometry progression result: %e" %data)            
