# Кол-во максимальных элементов в массиве.  
def GetMaxCount(Arr, N):
  Max = Arr[0]
  Count = 1

  I = 1
  while (I < N):
    if (Arr[I] > Max):
      Max = Arr[I]
      Count = 1
    else:
      if (Max == Arr[I]):
        Count += 1;
    
    I += 1

  return Count
