from utility import swap_if_needed
from utility import get_range
import random

def multiplication_question(level):
  """Generates a math question for multiplication at a specified level.

    Args:
        level (int): The difficulty level of the question. Higher levels
            correspond to larger number ranges.

    Returns:
        tuple: A tuple containing the first factor, second factor,
            and the product of the two factors.
  """
  # Get the minimum and maximum values for the specified level
  min, max = get_range(level)
  
  # Generate random factors within the specified range
  factors1 = random.randint(min, max)
  factors2 = random.randint(min, max)
  
  # Calculate the product (result of multiplication)
  result = factors1 * factors2
  return factors1, factors2, result