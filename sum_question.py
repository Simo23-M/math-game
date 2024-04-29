import random
from utility import get_range

def sum_question(level):
  """Generates a math question for addition at a specified level.

    Args:
        level (int): The difficulty level of the question. Higher levels
            correspond to larger number ranges.

    Returns:
        tuple: A tuple containing the first addend, second addend,
            and the sum of the two addends.
  """
  # Get the minimum and maximum values for the specified level
  min, max = get_range(level)
  
  # Generate random addend within the specified range
  addend1 = random.randint(min, max)
  addend2 = random.randint(min, max)
  
  # Calculate the sum 
  result = addend1 + addend2
  return addend1, addend2, result

