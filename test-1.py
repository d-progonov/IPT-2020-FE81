def solution(lists):
  if len(lists) == 1:
    return lists[0]

  ans = []
  first_list = lists.pop(0)
  for el in first_list:
    for lst in lists:
      if el in lst:
        ans.append(el)

  return ans

def main():
  lists = []
  N = int(input("N: "))
  for i in range(N):
    lists.append(input("lst {0}: ".format(i)).split(' '))
  print(solution(lists))    


if __name__ == "__main__":
  main()