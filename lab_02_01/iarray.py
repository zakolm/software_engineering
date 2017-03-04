def form_array(arr, n):
  new_arr = arr
  
  i = 0
  while (i < n):
    if (new_arr[i] < 0):
      new_arr.pop(i)
      n -= 1
    
    i += 1
    
  return new_arr, n


def print_array(arr, n):
  i = 0
  while (i < n):
    print(arr[i], end = " ")
    i += 1
  
  print("")
    
