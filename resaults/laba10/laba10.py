class Task:
    def __init__(self, size):
        self.size = size
        self.sol = 0
        self.solve()
  
    def solve(self):
        pos = [-1] * self.size
        self.putr(pos, 0)
        print("Найдено ", self.sol, " решений.")
    
    def putr(self, pos, target):
        if target == self.size:
            self.showboard(pos)
            self.sol += 1  
        else:
            for col in range(self.size):
                if self.checking(pos, target, col):
                    pos[target] = col
                    self.putr(pos, target + 1)
    
    def checking(self, pos, occupied, col):
        for i in range(occupied):
            if pos[i] == col:
                return False
        return True
    
    def showboard(self, pos):
        for row in range(self.size):
            line = ""
            for col in range (self.size):
                if pos[row] == col:
                    line += "T "
                else:
                    line += ". "
            print(line)
        print("\n")

def main():
    while True:
        try:
            n = int(input("Введите размер шахматной доски:"))
            if n <= 0:
                print("Размер должен быть положительным числом не равным нулю, введите правильное число!")
                continue
            break
        except ValueError:
            print("Введено неверное значение!")
    Task(n)
    
if __name__ == "__main__":
    main()
