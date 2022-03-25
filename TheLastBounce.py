import turtle
import time
import winsound
import pygame
import os
from pygame import mixer
import random
# Definisjoner


pygame.init()
mixer.init()

# definere poengsummer

spillerA = 0
spillerB = 0
delay = 0.01

# - Spillområdet

ball = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.tracer(0)
wn.title("Pong")
wn.bgcolor("black")
wn.bgpic("C:\\picc.gif")
wn.addshape("C:\\rube.gif")
wn.addshape("C:\\sverd.gif")

linje = turtle.Turtle()
linje.speed(0)
linje.color("white")
linje.hideturtle()
linje.penup()
linje.goto(0,-300)
linje.pendown()
linje.width(width=3)
linje.goto(0,275)



# - Rekkert nr. 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("C:\\sverd.gif")
paddle_a.penup()
paddle_a.goto(-350,0)


# - Rekkert nr. 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("C:\\sverd.gif")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball.shape("C:\\rube.gif")
ball.speed(0)
ball.penup()
ball.goto(0,0)


# tekst

poeng = turtle.Turtle()
poeng.speed(0)
poeng.color("white")
poeng.penup()
poeng.hideturtle()
poeng.goto(0,270)
poeng.write("The Last Bounce ",align="center",font =( 'ARCADECLASSIC',28,'normal'))

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)

# cord_a = turtle.Turtle()
# cord_a.speed(0)
# cord_a.color = ("green")
# cord_a.penup()
# cord_a.hideturtle()
# cord_a.goto(-350,-200)

# cord_b = turtle.Turtle()
# cord_b.speed(0)
# cord_b.color = ("green")
# cord_b.penup()
# cord_b.hideturtle()
# cord_b.goto(350, -200)

start = turtle.Turtle()
start.speed(0)
start.color("#cd9575")
start.penup()
start.hideturtle()
start.goto(0,0)


# Fysiske konstanter

dx = 2.3
dy = 2.3
ekstra = [1.8,1.5,1,-0.5,0.9,-0.7]
d = 3.3
i = 2.3
e = 1.1
##plus = random.choice([dx,dy])


# Funksjoner

b = [35]
a = [12.5]

# Hvor mye rekkertene skal bevege seg når x knapp presset

def paddle_a_up():
    
    if paddle_a.ycor() == 280:
        return
    y = paddle_a.ycor()
    y += b[0]
    paddle_a.sety(y)
    
def paddle_a_down():

    if paddle_a.ycor() == -280:
        return
    y = paddle_a.ycor()
    y -= b[0]
    paddle_a.sety(y)
    
def paddle_a_Right():

    if paddle_a.xcor() == -175:
        return
    
    x = paddle_a.xcor()
    x += a[0]
    paddle_a.setx(x)

def paddle_a_Left():

    if paddle_a.xcor() == -350:
        return
    
    x = paddle_a.xcor()
    x -= a[0]
    paddle_a.setx(x)
    
def paddle_b_up():

    if paddle_b.ycor() == 280:
        return
    y = paddle_b.ycor()
    y += b[0]
    paddle_b.sety(y)
    
def paddle_b_down():

    if paddle_b.ycor() == -280:
        return
    y = paddle_b.ycor()
    y -= b[0]
    paddle_b.sety(y)

def paddle_b_Right():

    if paddle_b.xcor() == 350:
        return
    
    x = paddle_b.xcor()
    x += a[0]
    paddle_b.setx(x)

def paddle_b_Left():
   
    if paddle_b.xcor() == 175:
        return
    
    x = paddle_b.xcor()
    x -= a[0]
    paddle_b.setx(x)
    
# Keyboard, wn står for window
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_Right, "d")
wn.onkeypress(paddle_a_Left, "a")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")
wn.onkeypress(paddle_b_Right, "l")
wn.onkeypress(paddle_b_Left, "j")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_a_Right, "D")
wn.onkeypress(paddle_a_Left, "A")
wn.onkeypress(paddle_b_up, "I")
wn.onkeypress(paddle_b_down, "K")
wn.onkeypress(paddle_b_Right, "L")
wn.onkeypress(paddle_b_Left, "J")
# Hovedrutine

winsound.PlaySound("C:\\321.",winsound.SND_ASYNC | winsound.SND_ALIAS)
time.sleep(0.8)
start.write(3,align="center", font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.8)
start.clear()
start.write(2,align="center", font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.9)
start.clear()
start.write(1,align="center", font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.9)
start.clear()
start.write("GO",align="center", font=('ARCADECLASSIC',70,'normal'))
time.sleep(1)
start.clear()



musikk=["C:\\Title.wav","C:\\hunt.wav",
        "C:\\leg.wav","C:\\dark.wav",
        "C:\\b.wav"]

current = []

def play():
    global current

    if not current:
        current = musikk[:]
        random.shuffle(current)
    
    song = current[0]
    current.pop(0)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

c = [1,-1]

engang = 0


while True:
    
    if not pygame.mixer.music.get_busy():
        play()
    wn.update()
    time.sleep(delay)
       
    # ---- RAMME START ---- #
    xb = ball.xcor()
    yb = ball.ycor()


    if engang == 0:
        string1 = "P1: {}"
        string_lengde1 = len(string1)+4
        print(string_lengde1)
        stringA = string1.ljust(string_lengde1)
        string2 = "P2: {}"
        string_lengde2 = len(string2)+4
        stringB = string2.rjust(string_lengde2)
        engang = 1
   
    stringC = stringA + stringB       
    
    if xb >= 370:
        xb = ball.xcor()*0
        yb = ball.ycor()*0
        dx  = dx * 0 + i * random.choice(c)
        dy  = dy * 0 + i * random.choice(c)
        pen.clear()
        spillerA += 1
        pen.write(stringC.format(spillerA,spillerB),align="center", font=('ARCADECLASSIC',24,'normal'))
        ball.clear()
        time.sleep(0.5)
        
        
        
    if xb <= -370:
        ball.clear()
        xb = ball.xcor()*0
        yb = ball.ycor()*0
        dx  = dx * 0 + i * random.choice(c)
        dy  = dy * 0 + i * random.choice(c)
        pen.clear()
        spillerB += 1
        pen.write(stringC.format(spillerA,spillerB),align="center", font=('ARCADECLASSIC',24,'normal'))
        ball.clear()
        time.sleep(0.5)
       
      
    if yb >= 280:
        winsound.PlaySound("C:\\sound.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.clear()
        dy *= -1 * e
        dx *= e
        ball.sety(280)
    
    if yb <= -280:
        winsound.PlaySound("C:\\sound.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.clear()
        dy *= -1 * e
        dx *= e
        ball.sety(-280)
        
##    if xb >= 380:
##        pen.write("P1: {} - P2: {}".format(spillerA, spillerB),align="center", font=('ARCADECLASSIC',24,'normal'))
##     
##    if xb <= -380:
##        pen.write("P1: {} - P2: {}".format(spillerA, spillerB),align="center", font=('ARCADECLASSIC',24,'normal'))
        
        
    if (ball.xcor() > paddle_b.xcor()-10 and ball.xcor() < paddle_b.xcor()+30) and ball.ycor() < paddle_b. ycor()+70 and ball.ycor() > paddle_b.ycor()-50:
        ball.clear()
        ball.setx(paddle_b.xcor()-30)
        winsound.PlaySound("C:\\ping.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        dx = dx * 0 + d *-1 - random.choice(ekstra)
        dy = dy * 0 + d * random.choice(c) + random.choice(ekstra)
##        plus += random.choice(ekstra)
##        plus -= random.choice(ekstra)
        
          
    if (ball.xcor() < paddle_a.xcor()+10 and ball.xcor() > paddle_a.xcor()-30) and ball.ycor() < paddle_a. ycor()+70 and ball.ycor() > paddle_a.ycor()-50:
        ball.clear()
        ball.setx(paddle_a.xcor()+30)
        winsound.PlaySound("C:\\ping.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        dx = dx * 0 + d + random.choice(ekstra)
        dy = dy * 0 + d * random.choice(c) + random.choice(ekstra)
##        plus += random.choice(ekstra)
##        plus -= random.choice(ekstra)
        
        
    # if spillerA == 1:
    #     winsound.PlaySound(r"C:\Users\Keezy\Downloads\fatality.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        
    # - Bevege ballen
    ball.setx(xb + dx ) 
    ball.sety(yb + dy )
    

    
      
          
    
          
    
     
