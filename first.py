import turtle
import os

# making a blank screen
#
scr = turtle.Screen()
scr.bgcolor("black")
scr.title("Space Invader")

#making the border
#
brd = turtle.Turtle()
brd.speed(0)
brd.color("white")
brd.penup()
brd.setposition(-300,-300)
brd.pendown()

i =1 
while i <= 4 :
    brd.fd(600)
    brd.left(90)
    i = i+1
brd.hideturtle()


# Making the player
plr = turtle.Turtle()
plr.speed(0)
plr.shape("triangle")
plr.color("blue")
plr.penup()
plr.setposition(0 , -250)
# plr.pendown()
plr.setheading(90)


# Making Thanos
# 
enemy = turtle.Turtle()
enemy.color("violet")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-250,250)




# Moving the player left
#
plr_speed = 15
def move_left() :
    x = plr.xcor()
    x -= plr_speed
    if x < -280 :
        x = -280
    plr.setx(x)

  


# Moving the player right
#
plr_speed = 15
def move_right() :
    x = plr.xcor()
    x += plr_speed
    if x > 280 :
        x = 280
    plr.setx(x)


#Read input from keyboard
#
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")

# thanos movement
enemy_speed = 2

while True :

    x = enemy.xcor()
    x += enemy_speed 
    enemy.setx(x)

    if enemy.xcor() > 270 :
        enemy_speed *= -1
   
    if enemy.xcor() < -270 :
        enemy_speed *= -1

    y = enemy.ycor()
    y -= 0.1
    enemy.sety(y)



turtle.mainloop 
delay = input("press enter to finish")