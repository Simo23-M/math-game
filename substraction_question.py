from utility import swap_if_needed
from utility import get_range
import random

def subtractions_question(level):
  """Generates a math question for subtraction at a specified level.

    Args:
        level (int): The difficulty level of the question. Higher levels
            correspond to larger number ranges.

    Returns:
        tuple: A tuple containing the minuend (number being subtracted from),
            subtrahend (number being subtracted), and the difference.
  """
  # Get the minimum and maximum values for the specified level
  min, max = get_range(level)
  
  # Generate random addend within the specified range
  sub1 = random.randint(min, max)
  sub2 = random.randint(min, max)
  
  # If the level is low swap 
  if level < 4:
    sub1, sub2 = swap_if_needed(sub1, sub2)
  
  # Calculate the substraction
  result = sub1 - sub2
  return sub1, sub2, result