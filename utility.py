def instruction():
    """ 
    Args: 
    
    Returns:
    Provide the instruction for the game
    """
    return "Answer the questions correctly and climb the levels!"

def swap_if_needed(sub1, sub2):
  """Swaps sub1 and sub2 if sub1 is less than sub2, ensuring sub1 is always larger or equal.

  Args:
      sub1 (int or float): The first number.
      sub2 (int or float): The second number.

  Returns:
      tuple: A tuple containing the swapped values (sub1, sub2), with sub1 being
              greater than or equal to sub2.
  """

  if sub1 < sub2:
    # Return the swapped values
    return sub2, sub1  
  else:
    # Return the original values if no swap is needed
    return sub1, sub2  



levels = {0:[1, 10], 1:[1, 20], 2:[1, 50], 3:[20, 100], 4:[0, 1000]}

def get_range(level):
  """
  Args: 
    level of the game
  
  Return:
    Range based on the game level
  """
  if level < len(levels):
    min, max = levels[level]
  else:
    # in case of the level is not in the dictionary return last level available
    min, max = levels[-1] 
  return min,max

