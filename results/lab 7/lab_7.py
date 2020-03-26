n = int(input('Enter number of characters: n = '))
s = input('Enter comma separated characters: ')
List = list(s.split(','))

sum = 0

for i in range (0, n-3):
    if List[i] == 'a' and List[i+1] == 'b' and List[i+2] == 'c':
        sum += 1
    if List[i] == 'a' and List[i+1] == 'b' and List[i+2] == 'a':
        sum += 1

print ('Number of occurrences of the group of letters "abc" and "aba":', sum)