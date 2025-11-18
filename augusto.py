import turtle
import random
t = turtle.Turtle()
turtle.Screen ().screensize(800,500)
turtle.tracer(False)

var = random.randint(0,100)

def laranja(var):
    t.speed(5)
    t.color("orange")
    t.begin_fill()
    t.circle (60)
    t.end_fill()
    caule(var)
    folha(var)

def folha(var):
    t.color("green")
    t.penup()
    t.left(90)
    t.forward(100)
    t.pendown()
    t.begin_fill()
    t.circle(60, 90)
    t.left(93)
    t.circle(60, 90)
    t.end_fill()

def caule(var):
    t.color("brown")
    t.begin_fill()
    t.circle(30,90)
    t.right(93)
    t.forward(5)
    t.right(60)
    t.circle(-30, 180)
    t.end_fill()

def folha(var):
    t.color("green")
    t.begin_fill()
    t.circle(60, 90)
    t.left(93)
    t.circle(60, 90)
    t.end_fill()

def spawnlaranja(cordX,cordY):
    t.penup()
    t.goto(cordX,cordY)
    t.pendown()
    size = random.randint(50,60)
    laranja(size)

turtle.onscreenclick(spawnlaranja,3)


turtle.done()