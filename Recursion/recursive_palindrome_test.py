def is_palindrome(my_string):
  if len(my_string) <= 1:
    return True
  else:
    return my_string[-1] == my_string[0] and is_palindrome(my_string[1:-1])



# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)