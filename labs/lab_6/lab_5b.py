def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def in_data():
    try:
        b = float(input("Please enter a first element of geometry progression(b): "))
        q = float(input("Please enter a geometry progression koeficient(q): "))
        n = int(input("Please enter an integer number of last element(bigger than 0): "))
        
        if n == 0:
            raise Exception("Please, enter a number of element, bigger than 0")
        
        return b, q, n
    
    except ValueError:
        print("Please, enter a numeric data.")
        exit_func()
        in_data()
    
    except Exception as e:
        print(e)
        exit_func()
        in_data()

def geom_progression(b, q, n, sum1 = 0):
    if n > 0 :
        sum1 += b
        b *= q
        n -= 1
        return geom_progression(b, q, n, sum1)
    else:
        return sum1

if __name__ == "__main__":
    b, q, n = in_data()
    print("The sum of elements is: ", geom_progression(b, q, n) )
