from rich.console import Console
import random
import banner

console = Console()
console.print(banner.get_banner(), style="bold red")

def instruction():
    return "Answer the questions correctly and climb the levels!"

levels = {0:[1, 10], 1:[1, 20], 2:[1, 50], 3:[20, 100]}

def sum_question(level):
    min, max = levels[level]
    addend1 = random.randint(min, max)
    addend2 = random.randint(min, max)
    result = addend1 + addend2
    return addend1, addend2, result

def subtractions_question(level):
    min, max = levels[level]
    addend1 = random.randint(min, max)
    addend2 = random.randint(min, max)
    result = addend1 - addend2
    return addend1, addend2, result

def create_question(level):
    match level:
        case 0:
            console.print("Easy level")
        case _:
            console.print(f"Level number {level}")

first_time = input("Is this your first time playing? [y/n]")

if (first_time == "y"):
    console.print(instruction())

console.print("Let's go!!", style="bold blue")

game_level = 0
game_error = 0
user_res = 0
for i in range(10):
    console.print(f"Question number: {i+1}", style="bold blue")
    add1, add2, res = sum_question(game_level)
    result = input(f"{add1} + {add2} = ")

    if result.isdigit():  # Check if all characters are digits
      user_res = int(result)
    else:
      print("Invalid input. Please enter an integer.")

    if user_res != res:
        game_error += 1
        console.print(f"Oh no! it's wrong, error number: {game_error}")
        if game_error == 2:
            console.print("Too much error, retry")
            break

for i in range(10):
    console.print(f"Question number: {i+1}", style="bold blue")
    add1, add2, res = subtractions_question(game_level)
    result = input(f"{add1} + {add2} = ")

    if result.isdigit():  # Check if all characters are digits
      user_res = int(result)
    else:
      print("Invalid input. Please enter an integer.")

    if user_res != res:
        game_error += 1
        console.print(f"Oh no! it's wrong, error number: {game_error}")
        if game_error == 2:
            console.print("Too much error, retry")
            break



