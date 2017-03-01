from iarray import *

def Test1():
  Arr = list()
  
  Arr.append(5)
  Arr.append(3)
  Arr.append(2)
  Arr.append(5)
  Arr.append(1)
  
  return Arr, 5


def main():
  Arr, N = Test1()
  
  print("Maximal value is found " + str(GetMaxCount(Arr, N)) + " times.")


if __name__ == '__main__':
  main()