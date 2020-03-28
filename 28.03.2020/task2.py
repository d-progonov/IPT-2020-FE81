import numpy as np

s = "a b c d e f g h i j k l m n o p r q r s t u v w x y z a b c d e f g h i j k l m n o p r q r s t u v w x y z a b c d e f g h i j k l m n o p r q r s t u v w x y z"
List = list(s.split())
print(List)

st = str(input())
ls = list(st.split("Уведите строку:"))
n = 5
k = np.size(ls)
# Шифрування
for i in range(0, k):
    ls[i] = List[i + 5]
print(ls)

# Дешифрування
for i in range(0, k):
    ls[i] = List[26 + i - 5]
print(ls)
