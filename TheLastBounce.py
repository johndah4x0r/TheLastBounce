import turtle
import time
import pygame
import os
import sys
from pygame import mixer
import random

# Miljø
pygame.init()
mixer.init()

# - Lydkanaler: 1 musikk-kanal og 4 vilkårlige kanaler
scm = pygame.mixer.music
scl = [pygame.mixer.find_channel() for _ in range(4)]

# Definisjoner

# - Baner
PATHS = {
    "bgpic":    "./res/gif/picc.gif",
    "rube":     "./res/gif/rube.gif",
    "sword":    "./res/gif/sword.gif",
    "count":    "./res/wav/count.wav",
    "bounce":   "./res/wav/bounce.wav",
    "ping":     "./res/wav/ping.wav",
    "bgwav": [
        "./res/wav/title.wav",
        "./res/wav/hunt.wav",
        "./res/wav/leg.wav",
        "./res/wav/dark.wav",
        "./res/wav/b.wav",
    ],
}

# - Taster
KEYS = {
    "a_up":     ["w", "W"],
    "a_down":   ["s", "S"],
    "a_left":   ["a", "A"],
    "a_right":  ["d", "D"],
    "b_up":     ["i", "I"],
    "b_down":   ["k", "K"],
    "b_left":   ["j", "J"],
    "b_right":  ["l", "L"],
}

# - Bildefrekvens
DELAY = 1.67e-2

# Definere poengsummer
spillerA = 0
spillerB = 0


# Objekter

# - Spillområdet

ball = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.tracer(0)
wn.title("Pong")
wn.bgcolor("black")
wn.bgpic(PATHS['bgpic'])
wn.addshape(PATHS['rube'])
wn.addshape(PATHS['sword'])

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
paddle_a.shape(PATHS['sword'])
paddle_a.penup()
paddle_a.goto(-350,0)


# - Rekkert nr. 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape(PATHS['sword'])
paddle_b.penup()
paddle_b.goto(350,0)


# - Ball
ball.shape(PATHS['rube'])
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


info = turtle.Turtle()
info.ht()
info.penup()
info.goto(270,-270)
info.color("#cd9575")
info.speed(0)


# Fysiske konstanter
dx = 2.3
dy = 2.3
ekstra = [1.8,1.5,1,0.9,-0.5,-0.7]
d = 3.3
i = 2.3
e = 1.1

pad_dx = 12.5
pad_dy = 35

c = [1,-1]

# Bevegelsesknapper

def key_a_up():
    if paddle_a.ycor() == 280:
        return

    y = paddle_a.ycor()
    y += pad_dy
    paddle_a.sety(y)
    
def key_a_down():
    if paddle_a.ycor() == -280:
        return

    y = paddle_a.ycor()
    y -= pad_dy
    paddle_a.sety(y)
    
def key_a_right():
    if paddle_a.xcor() == -175:
        return
    
    x = paddle_a.xcor()
    x += pad_dx
    paddle_a.setx(x)

def key_a_left():
    if paddle_a.xcor() == -350:
        return
    
    x = paddle_a.xcor()
    x -= pad_dx
    paddle_a.setx(x)
    
def key_b_up():
    if paddle_b.ycor() == 280:
        return

    y = paddle_b.ycor()
    y += pad_dy
    paddle_b.sety(y)
    
def key_b_down():
    if paddle_b.ycor() == -280:
        return

    y = paddle_b.ycor()
    y -= pad_dy
    paddle_b.sety(y)

def key_b_right():
    if paddle_b.xcor() == 350:
        return
    
    x = paddle_b.xcor()
    x += pad_dx
    paddle_b.setx(x)

def key_b_left():
    if paddle_b.xcor() == 175:
        return
    
    x = paddle_b.xcor()
    x -= pad_dx
    paddle_b.setx(x)


for k in KEYS.keys():
    # Hent funksjonen
    fun = eval("key_%s" % k)

    # Bind funksjonen til tastene definert ved 'KEYS'
    wn.onkeypress(fun, KEYS[k][0])
    wn.onkeypress(fun, KEYS[k][1])

# Start å lytte
wn.listen()


# Musikk-avsplling

# - Spilleliste
current = []

# - Asynkron avspilling
def playsnd(f):
    if not os.path.exists(f):
        return

    s = mixer.Sound(f)

    # Finn ledig kanal
    for k in scl:
        if not k.get_busy():
            k.play(s)
            break
    else:
        print(" W: Gikk tom for lydkanaler.", file=sys.stderr)

def play_bg():
    global current

    # Hopp over dersom det allerede avspilles musikk
    if pygame.mixer.music.get_busy():
        return

    if not current:
        current = PATHS['bgwav'][:]
        random.shuffle(current)
    
    song = current.pop()

    if os.path.exists(song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()


# ---- Hovedrutine ---- #

string1 = "P1: {}"
stringA = string1.ljust(len(string1) + 4)
string2 = "P2: {}"
stringB = string2.rjust(len(string2) + 4)
stringC = stringA + stringB

# - Nedtelling
playsnd(PATHS['count'])
time.sleep(0.8)

start.write(3,align="center",font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.8)
start.clear()
start.write(2,align="center",font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.9)
start.clear()
start.write(1,align="center",font=('ARCADECLASSIC',50,'normal'))
time.sleep(0.9)
start.clear()
start.write("GO",align="center",font=('ARCADECLASSIC',70,'normal'))
time.sleep(1)
start.clear()

# - Hovedløkke

m = ""

while True:
    # ---- RAMME START ---- #
    t1 = time.time()

    info.clear()
    info.write(m,align="center")

    # Bytt musikk når det er mulig
    play_bg()

    # Hent ballens posisjon
    p0 = [ball.xcor(),ball.ycor()]
    
    # Primitiv kollisjonssporing
    # TODO: Litt hjelp, takk...

    # - Når ballen treffer spillerens side
    if abs(p0[0]) >= 370:
        # Flytt ballen til midten
        ball.setx(0)
        ball.sety(0)

        # Endre retning
        (dx,dy) = (i*random.choice(c),i*random.choice(c))

        # Oppdater oversikt
        if p0[0] > 0:
            spillerA += 1
        else:
            spillerB += 1
        
        ball.clear()
        pen.clear()
        pen.write(
            stringC.format(spillerA,spillerB),
            align="center",
            font=('ARCADECLASSIC',24,'normal')
            )

        wn.update()
        time.sleep(0.5)
        continue

    # - Når ballen treffer taket eller gulvet
    if abs(p0[1]) >= 280:
        # Spill lyd
        playsnd(PATHS['bounce'])
        
        # Endre retning
        dx = (dx*e) if abs(dx*e) < 3.3 else dx
        dy = (-dy*e) if abs(dy*e) < 3.3 else -dy

        # Avgrens ballen
        if p0[1] > 0:
            p0[1] = 280
        else:
            p0[1] = -280

    # - Når ballen treffer rekkert

    pa = (paddle_a.xcor(),paddle_a.ycor())
    pb = (paddle_b.xcor(),paddle_b.ycor())

    if (pb[0] - 10 < p0[0] < pb[0] + 30) and (pb[1] - 50 < p0[1] < pb[1] + 70):
        playsnd(PATHS['ping'])

        ball.clear()
        p0[0] = pb[0] - 30

        dx = -d - random.choice(ekstra)
        dy = d * random.choice(c) + random.choice(ekstra)

    if (pa[0] - 30 < p0[0] < pa[0] + 10) and (pa[1] - 50 < p0[1] < pa[1] + 70):
        playsnd(PATHS['ping'])

        ball.clear()
        p0[0] = pa[0] + 30

        dx = d + random.choice(ekstra)
        dy = d * random.choice(c) + random.choice(ekstra)

    # - Bevege ballen
    ball.setx(p0[0] + dx) 
    ball.sety(p0[1] + dy)
    
    # Oppdater innhold
    wn.update()

    # Sett bildefrekvens til 1/DELAY
    t2 = time.time()
    s = DELAY-(t2-t1) if (t2-t1) < DELAY else 0.0
    time.sleep(s)
    t3 = time.time()

    m = "FPS: %.2f (%.2f ms)  FT: %.2f ms" % (1/(t3-t1),1.0e3*(t3-t1),1.0e3*(t2-t1))