### This is the file where we are going to edit the code from the Typing Game. ###

from random import choice, randrange
# Nicholas Lee (NL) #21082020, imported uppercase letters
from string import ascii_letters
from turtle import *

from freegames import vector

targets = []
letters = []
score = 0
speed = 100
lives = 3

def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200

#NL made a function to draw the score onto the screen 
def draw_score():
    global score
    goto(-150, 175)
    scorekeeper = "Score: " + str(score)
    write(scorekeeper, align='center', font=('Helvetica', 20, 'normal'))

def draw_lives():
    global lives
    goto(150, 175)
    lives_counter = "Lives: " + str(lives)
    write(lives_counter, align='center', font=('Helvetica', 20, 'normal'))
    

def draw():
    """Draw letters."""
    clear()
    #NL draws the score onto the screen with the letters
    draw_score()
    # CS draws the lives onto the screen with the letters
    draw_lives()
    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        write(letter, align='center', font=('Helvetica', 20, 'normal'))

    update()


# CS made a game over screen that appears once you lose your three lives

def game_over():

    clear()

    text = 'Game Over :('
    goto(0,0)
    write(text, align='center', font=('Helvetica', 20, 'normal'))

    update()

    

def move():

    """Move letters."""
    global speed
    global lives
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_letters)

        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()
    '''
    for target in targets:
        if not inside(target):
            return
    '''
    # CS made game end once three lives are up
    for target in targets:
        if not inside(target):
            lives -= 1
            pos = targets.index(target)
            del targets[pos]
            del letters[pos]

        if lives <= 0:
           
            game_over()

            return

    ontimer(move, speed)


def press(key):
    """Press key."""
    global score
    global speed
    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    #NL added speed increase for every letter you get right
        while speed>15:
            speed -=5

    else:
        score -= 1
        speed +=5
    print('Score:', score)



setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
#NL added uppercase letters 
for letter in ascii_letters:
    onkey(lambda letter=letter: press(letter), letter)
move()
done()