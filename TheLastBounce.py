import turtle
import time
import winsound
import pygame
import os
from pygame import mixer
import random

pygame.init()
mixer.init()

# Definere poengsummer
spillerA = 0
spillerB = 0

delay = 0.01

# Objekter

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


# - Ball

ball.shape("C:\\rube.gif")
ball.speed(0)
ball.penup()
ball.goto(0,0)


# - Tekst

poeng = turtle.Turtle()
poeng.speed(0)
poeng.color("white")
poeng.penup()
poeng.hideturtle()

poeng.goto(0,270)
poeng.write(
    "The Last Bounce ",
    align="center",
    font=('ARCADECLASSIC',28,'normal')
    )

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)

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

b = 35
a = 12.5
c = [1,-1]

# Bevegelsesknapper

def paddle_a_up():
    
    if paddle_a.ycor() == 280:
        return
    y = paddle_a.ycor()
    y += b
    paddle_a.sety(y)
    
def paddle_a_down():

    if paddle_a.ycor() == -280:
        return
    y = paddle_a.ycor()
    y -= b
    paddle_a.sety(y)
    
def paddle_a_Right():

    if paddle_a.xcor() == -175:
        return
    
    x = paddle_a.xcor()
    x += a
    paddle_a.setx(x)

def paddle_a_Left():

    if paddle_a.xcor() == -350:
        return
    
    x = paddle_a.xcor()
    x -= a
    paddle_a.setx(x)
    
def paddle_b_up():

    if paddle_b.ycor() == 280:
        return
    y = paddle_b.ycor()
    y += b
    paddle_b.sety(y)
    
def paddle_b_down():

    if paddle_b.ycor() == -280:
        return
    y = paddle_b.ycor()
    y -= b
    paddle_b.sety(y)

def paddle_b_Right():

    if paddle_b.xcor() == 350:
        return
    
    x = paddle_b.xcor()
    x += a
    paddle_b.setx(x)

def paddle_b_Left():
   
    if paddle_b.xcor() == 175:
        return
    
    x = paddle_b.xcor()
    x -= a
    paddle_b.setx(x)

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_a_Right, "d")
wn.onkeypress(paddle_a_Right, "D")
wn.onkeypress(paddle_a_Left, "a")
wn.onkeypress(paddle_a_Left, "A")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_up, "I")
wn.onkeypress(paddle_b_down, "k")
wn.onkeypress(paddle_b_down, "K")
wn.onkeypress(paddle_b_Right, "l")
wn.onkeypress(paddle_b_Right, "L")
wn.onkeypress(paddle_b_Left, "j")
wn.onkeypress(paddle_b_Left, "J")
wn.listen()

# Nedtelling
winsound.PlaySound(
    "C:\\321.",
    winsound.SND_ASYNC | winsound.SND_ALIAS
    )
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


# Musikk-avsplling
# - Asynkron avspilling

musikk = [
    "C:\\Title.wav",
    "C:\\hunt.wav",
    "C:\\leg.wav",
    "C:\\dark.wav",
    "C:\\b.wav",
    ]

# - Spilleliste
current = []

def play():
    global current

    if not current:
        current = musikk[:]
        random.shuffle(current)
    
    song = current.pop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


string1 = "P1: {}"
stringA = string1.ljust(len(string1) + 4)
string2 = "P2: {}"
stringB = string2.rjust(len(string2) + 4)
stringC = stringA + stringB


while True:
    # Bytt musikk når det er mulig
    if not pygame.mixer.music.get_busy():
        play()
    
    # ---- RAMME START ---- #

    # Hent ballens posisjon
    p0 = [ball.xcor(),ball.ycor()]
    
    # - Når ballen treffer spillerens side
    if abs(p0[0]) >= 370:
        # Flytt ballen til midten
        ball.setx(0)
        ball.sety(0)

        # Start med tilfeldig retning
        dx = random.choice(c)
        dy = random.choice(c)

        # Oppdater oversikt
        if p0[0] > 0:
            spillerA += 1
        else:
            spillerB += 1
        
        ball.clear()
        pen.clear()
        pen.write(
            stringC.format(spillerA, spillerB),
            align="center",
            font=('ARCADECLASSIC',24,'normal')
            )

        wn.update()
        time.sleep(0.5)
        continue

    # - Når ballen treffer taket eller gulvet
    if abs(p0[1]) >= 280:
        # Spill lyd
        winsound.PlaySound(
            "C:\\sound.wav",
            winsound.SND_ASYNC | winsound.SND_ALIAS
            )
        
        # Endre retning
        dx *= e
        dy *= -e

        # Avgrens ballen
        if p0[1] > 0:
            p0[1] = 280
        else:
            p0[1] = -280

    
    # - Når ballen treffer rekkert
    #   TODO: Implementer kollisjondetektering
    pa = (paddle_a.xcor(),paddle_a.ycor())
    pb = (paddle_b.xcor(),paddle_b.ycor())

    if (pb[0] - 10 < p0[0] < pb[0] + 30) and (pb[1] - 50 < p0[1] < pb[1] + 70):
        winsound.PlaySound(
            "C:\\ping.wav",
            winsound.SND_ASYNC | winsound.SND_ALIAS
            )

        ball.clear()
        p0[0] = pb[0] - 30

        dx = -d - random.choice(ekstra)
        dy = d * random.choice(c) + random.choice(ekstra)

    if (pa[0] - 30 < p0[0] < pa[0] + 10) and (pa[1] - 50 < p0[1] < pa[1] + 70):
        winsound.PlaySound(
            "C:\\ping.wav",
            winsound.SND_ASYNC | winsound.SND_ALIAS
            )

        ball.clear()
        p0[0] = pa[0] + 30

        dx = d + random.choice(ekstra)
        dy = d * random.choice(c) + random.choice(ekstra)

    # - Bevege ballen
    ball.setx(p0[0] + dx) 
    ball.sety(p0[1] + dy)
    
    wn.update()
    time.sleep(delay)