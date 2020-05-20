a = int(input("Enter number: "))
c = int(input("Enter number: "))
m = int(input("Enter number: "))
def funcF(n):
    if(n >= 0 and n <= 9):
        return n
    else:
        n = funcG(n)*funcF(n - 1 - funcG(n)) + n
    return n
def funcG(n):
    g = (a*(n-c)) % 10
    return g

def main():
    try:
        if(m >= 0 or c >= 0 or a >= 0):
            print(funcF(m))
        else:
            print("Wrong data type")
    except ValueError or Exception:
        print("Wrong data type")
if __name__ == "__main__":
      main()
