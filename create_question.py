from sum_question import sum_question
from substraction_question import subtractions_question
from multiplication_question import multiplication_question
from division_question import division_question
import random

def create_question(level, console):
  operations = ["+", "-", "*", "/"]
  operation = ""
  if level < 4:
    operation = operations[level]
  else:
    operation = random.choice(operations)
   
  match operation:
    case "+":
      user_res = 0
      add1, add2, res = sum_question(level)
      
      try:
        user_res = int(input(f"{add1} + {add2} = "))
      # Use user_number here
      except ValueError:
        console.print("Invalid input. Please enter a number.", style="bold red")
             
      if user_res != res:
        return False
    
    case "-":
      user_res = 0
      sub1, sub2, res = subtractions_question(level)
      try:
        user_res = int(input(f"{sub1} - {sub2} = "))
      # Use user_number here
      except ValueError:
        console.print("Invalid input. Please enter a number.", style="bold red")
             
      if res != user_res:
        console.print(f"The right result was: {res} {user_res}")
        return False
    
    case "*":
      user_res = 0
      f1, f2, res = multiplication_question(level)
      try:
        user_res = int(input(f"{f1} * {f2} = "))
      # Use user_number here
      except ValueError:
        console.print("Invalid input. Please enter a number.", style="bold red")
             
      if res != user_res:
        console.print(f"The right result was: {res} {user_res}")
        return False
    
    case "/":
      user_res = 0
      d1, d2, res = division_question(level)
      try:
        user_res = int(input(f"{d1} / {d2} = "))
      # Use user_number here
      except ValueError:
        console.print("Invalid input. Please enter a number.", style="bold red")
             
      if res != user_res:
        console.print(f"The right result was: {res} {user_res}")
        return False        
      
  
  return True