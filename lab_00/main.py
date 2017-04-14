from iarray import *

# Тестирование первоначальное.  
def Test1():
  Arr = list()
  
  Arr.append(5)
  Arr.append(3)
  Arr.append(2)
  Arr.append(5)
  Arr.append(1)
  
  return Arr, 5

# Тестирование студента.
def Test2():
  Arr = list()

  Arr.append(1)
  Arr.append(1)
  Arr.append(1)
  Arr.append(5)

  return Arr, 4


def main():
  Arr, N = Test1()
  
  print("Maximal value is found " + str(GetMaxCount(Arr, N)) + " times.")

  #
  Arr, N = Test2()

  print("[Test2] Maximal value is found " + str(GetMaxCount(Arr, N)) + " times.")

if __name__ == '__main__':
  main()
