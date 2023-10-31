###  COMMENTING DONE BY CAMDEN DA SILVA, ID: 21058783 ###

"""Game to practice typing.

Exercises

1. Change the speed of letters.
2. Add uppercase letters.
3. Make the game faster as the score gets higher.
4. Make the letters more frequent as the score gets higher.
"""
# here the program is taking functions from modules: random, string, turtle and freegames
from random import choice, randrange # randrange and choice returns a randomly selected variable from a range
from string import ascii_lowercase # ascii_lowercase will change any letter to lowercase
from turtle import * # turtle is a graphics method, importing * brings all the names from the module turtle.

from freegames import vector

targets = [] # this will mark the position of the falling letters (changing over time)
letters = [] # this is the list that stores exactly what letters are going to fall down the screen
score = 0 # this will keep track of the score of the player (score += 1 each time the player gets a point, opposite when the fail


def inside(point):
   # this functions seems to check to see if a given point is on the screen (-200, 200). if it is the function will return true
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw():
    # using the turtle module the function will draw the falling letters on the screen
    # steps:
    # 1. clears the screen
    # 2. goes through the targets and the letters lists, the function appears the aformentioned letters and targets on the screen
    # 3. updates the screen
    """Draw letters."""
    clear()

    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        write(letter, align='center', font=('Consolas', 20, 'normal'))

    update()


def move():
    # this move function moves the letters randomly around the screen
    # First it chooses a number (at random) that will fall
    # The function then assigns the x coordinate and adds it to 'target' list, and the randomly chosen letter to the 'letter' list.   

    """Move letters."""
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)
# the function here moves the target letter down 1 y-position, then updates the screen

    for target in targets:
        target.y -= 1

    draw()
# now it checks to see if any target letter leaves the screen. if so it ends the game
    for target in targets:
        if not inside(target):
            return
# now it sets a timer for a delay until the game loop starts again. 
    ontimer(move, 100)

# this is the fucntion that handles user input keys
def press(key):
    """Press key."""
    global score

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    print('Score:', score)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
for letter in ascii_lowercase:
    onkey(lambda letter=letter: press(letter), letter)
move()
done()