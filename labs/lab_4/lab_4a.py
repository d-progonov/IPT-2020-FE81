def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def in_data():
    try:
        m = int(input("Please enter the width of matrix: "))
        n = int(input("Please enter the height of matrix: "))
        
        if m < 1 or n < 1:
            raise ValueError

        return m, n
    except ValueError:
        print("\nYou have entered a wrong data.\nPlease repeat your input using only integer numbers bigger then 0.")
        exit_func()


m, n = in_data()

matrix = [[0]*m for i in range(n)]
sum = -3
l = 0
amount = m*n
iter = -1

for v in range(n-1, 0, -1):

    for i in range(l-1, m-1-l):
        if iter == amount:
            break
        matrix[v][i] = sum
        sum += 3
        iter += 1

    for i in range(v, n-v-1, -1):
        if iter == amount:
            break
        matrix[i][m - l - 1] = sum
        sum += 3
        iter += 1
        if iter == amount:
            break

    for i in range(m-1-l, 0+l , -1):
        if iter == amount:
            break
        matrix[n-v-1][i] = sum 
        sum += 3
        iter += 1
        if iter == amount:
            break

    for i in range(n-v-1, v-1):
        if iter == amount:
            break
        matrix[i][l] = sum 
        sum += 3
        iter += 1
        if iter == amount:
            break

    if iter == amount:
        break

    l += 1



for i in matrix:
    print(*i)


