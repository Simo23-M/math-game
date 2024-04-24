NUM_LINES_TO_CLEAR = 5  # You can adjust this value

def clear_previous_lines():
  """Moves the cursor up and overwrites previous lines."""
  cursor_up = "\033[" + str(NUM_LINES_TO_CLEAR) + "A"  # ANSI escape sequence for cursor up
  clear_line = "\033[K"  # ANSI escape sequence to clear current line
  print(cursor_up * NUM_LINES_TO_CLEAR + clear_line * NUM_LINES_TO_CLEAR)

# Example usage
print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
print("Line 5")

clear_previous_lines()

print("This is a new message after clearing some lines.")