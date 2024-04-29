from rich.console import Console
from utility import instruction
from create_question import create_question
import banner

console = Console()
console.print(banner.get_banner(), style="bold red")

first_time = console.input("Is this your first time playing? \[y/n]")

if (first_time == "y"):
  console.print(instruction())

console.print("Let's go!!", style="bold blue")

game_level = 0
game_error = 0
point = 0
while game_error != 2:
  for i in range(10):
    # User provide wrong answer
    if create_question(game_level, console) == False: 
      game_error += 1
      console.print(f"Oh no! it's wrong, error number: {game_error}")
      if game_error == 2:
        console.print("Too much error, retry")
        break
    else:
      point += 1 * int(game_level / 5)
  game_level += 1
  game_error = 0

