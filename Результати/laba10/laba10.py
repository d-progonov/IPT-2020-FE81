class RookTask:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()
  
    def solve(self):
        positions = [-1] * self.size
        self.put_rook(positions, 0)
        print("Found", self.solutions, "solutions.")
    
    def put_rook(self, positions, target_row):
        if target_row == self.size:
            self.show_full_board(positions)
            self.solutions += 1 
            
        
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_rook(positions, target_row + 1)
    
    def check_place(self, positions, occupied_rows, column):
        for i in range(occupied_rows):
            if positions[i] == column:
                return False
        return True
    
    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range (self.size):
                if positions[row] == column:
                    line += "T "
                else:
                    line += ". "
            print(line)
        print("\n")

def main():
    while True:
        try:
            n = int(input("Input your chess deck size:"))
            if n <= 0:
                print("There will be no solutions with size = '0' or any non-positive number! Please, input another size!")
                continue
            break
        except ValueError:
            print("Invalid value entered!")
    RookTask(n)
    
if __name__ == "__main__":
    main()
