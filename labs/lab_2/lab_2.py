def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def comparison():
    try:
        x = float(input("Please, input x number: "))
        z = float(input("Please, input z number: "))
        y = float(input("Please, input y number: "))
        if x < z :
            if x == y:
                print("Minimum is x which equal to y:", x)
            elif x < y:
                print("Minimum x:", x)
        elif y < x:
            if y == z:
                print("Minimum is y which is equal to z:", y)
            elif y < z:
                print("Minimum is y:", y)
        elif z < x:
            if z == y:
                print("Minimum is z which is equal to y:", y)
            elif z < y:
                print("Minimum is z:", z)
        else:
            print("All numbers are equal.")

    except ValueError:
        print("\nYou have to enter only a number. Please, repeat your input.")
        exit_func()
        comparison()

if __name__ == "__main__":
    comparison()
