# Space Invaders

import turtle
import math
import random
import os

# set up screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("images/space_invaders_background.gif")

# Register the shapes

wn.addshape("images/invader.gif")
wn.addshape("images/player.gif")

# Draw a Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to 0
score = 0

# Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: %s"%score
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create a player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("images/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


playerSpeed = 15

# Create the Enemy
# choose a number of enemies
numberOfEnemies = 5
# create empty list of enemies
enemies = []
# add enemies to the list
for i in range(numberOfEnemies):
    # Create enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("images/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 2

# Create player's bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is fired

bulletState = "ready"


# Move the player Left and Right


def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # declare bulletState as a global if it needs changed
    global bulletState
    if bulletState == "ready":
        os.system("afplay sounds/laser.wav&")
        bulletState = "fire"
        # move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create Keyboard Bindings


wn.onkey(move_left,"Left")

wn.onkey(move_right,"Right")

wn.onkey(fire_bullet,"space")


wn.listen()



# Main Game Loop
while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        # Move the enemy Back and Down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemySpeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemySpeed *= -1
        # check if enemy and bullet have collided
        if isCollision(enemy, bullet):
            os.system("afplay sounds/explosion.wav&")
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            # reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update Score
            score += 10
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        # check if enemy hits player
        if isCollision(player, enemy):
            os.system("afplay sounds/explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    # check to see if bullet has hot the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"





