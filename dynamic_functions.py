def check_3Digits(list1):
  # return number in range(100,1000)
  three_digit_list = []
  for n in list1:
    if n in range(100,1000):
      three_digit_list.append(n)
      return True
    else:
      pass
  return three_digit_list

    #the reason we cannot put in "return False" is because it will return False
      #even when one number is not in the range.
      #for the numbers 55,66,600, the first 2 will be passed but the last one is True
  #we can return False but it has to be outside the loop.
      
  # pass
  
########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(numbers):
  for n in numbers:
    if n in range(0,9999999):
      return True
    else:
      pass
  return False
  
    
  


########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.
def sum_less(numbers2):
  for n in numbers2:
    if n in range(0,1000):
      total = sum(numbers2)
    return total
  else:  
    pass

########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
