def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def num_sum():
    try:
        res = 0
        i = 1

        n = int(input("Please, enter the integer number of last element: "))
        
        while i <= n:
            res = res + 1/((3 * i - 2)*(3 * i + 1))
            i += 1

        print("The sum of number series with %d elements is: %.4f" % (n, res))

    except ValueError:
        print("\nPlease enter only an integer. \nRepeat your input.\n")
        exit_func()
        num_sum()

if __name__ == "__main__":
    num_sum()
