A = []
for i in range (0, 1024):
  A.append(i)
  
print(A)

print("\n")
print("\n")

B = []
for elem in A:
  b = elem.to_bytes((elem.bit_length() // 8) + 1, byteorder='little')
  B.append(b)
  
print(B)

# here must be:
'''
Найти самую длинную непрерывную последовательность единиц и определить индексы первого и последнего элементов в ней. 
Методы обработки строк не используются.
'''
