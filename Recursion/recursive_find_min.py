def find_min(my_list):
  if len(my_list) == 0:
    return None
  elif len(my_list) == 1:
    return my_list[0]
  else:
    rest = find_min(my_list[1:])
    if my_list[0] < rest:
      return my_list[0]
    else: 
      return rest

  



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)