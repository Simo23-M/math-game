from utility import swap_if_needed
from utility import get_range
import random

def division_question(level):
    """Generates a math question for division at a specified level.

    Args:
        level (int): The difficulty level of the question. Higher levels
            correspond to larger number ranges.

    Returns:
        tuple: A tuple containing the dividend (number being divided),
            divisor (number dividing the dividend), and the quotient (result of division).
    """

    # Get the minimum and maximum values for the specified level
    min_value, max_value = get_range(level)

    # Generate random dividend and divisor within the specified range
    dividend = random.randint(min_value, max_value)
    divisor = random.randint(min_value, max_value)

    # Ensure the divisor is not zero to avoid division by zero errors
    dividend, divisor = swap_if_needed(dividend, divisor)

    # Calculate the quotient (result of division)
    result = dividend / divisor

    return dividend, divisor, result
