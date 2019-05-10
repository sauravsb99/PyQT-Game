import turtle
import os
import math
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


#Making Infinity stones
#
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
# bullet.setposition(plr.xcor(),plr.ycor()+15)

# Collision condition
#
def Collision(t1,t2):
    z = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2) )
    if z < 20 :
        return True
    else :
        return False
    


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


bullet_speed = 20
bullet_status = "ready"

# Bullet Movement
#
def fire() :
    global bullet_status
    if(bullet_status == "ready"): 
        bullet_status = "fire"
        x = plr.xcor()
        y = plr.ycor() + 15
        bullet.setposition(x,y)
        bullet.showturtle()



#Read input from keyboard
#
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire,"space")

# thanos movement
enemy_speed = 8

while True :

    x = enemy.xcor()
    x += enemy_speed 
    enemy.setx(x)

    if enemy.xcor() > 270 :
        enemy_speed *= -1
   
    if enemy.xcor() < -270 :
        enemy_speed *= -1

    y = enemy.ycor()
    y -= 0.4
    enemy.sety(y)

#move the bullet
#
    if bullet_status == "fire" :
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275 :
        bullet.hideturtle()
        bullet_status = "ready"

    if (Collision(bullet, enemy)):
        enemy.setposition(-250 , 250)
        bullet.hideturtle()
        bullet_status="ready"

    if (Collision(plr, enemy)):
        plr.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break



turtle.mainloop 
delay = input("press enter to finish")