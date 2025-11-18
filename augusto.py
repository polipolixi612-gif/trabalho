import turtle
tela = turtle.Screen()
tela.title("Clique para aparecer uma maça")
tela.bgcolor("White")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def desenhar_maça(x, y):
    t.penup()
    t.goto(x, y - 40)
    t.pendown()

    t.color("red")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.color("black")
    t.pensize(5)
    t.setheading(90)
    t.forward(20)

    t.color("green")
    t.begin_fill()
    t.circle(15, 90)
    t.left(90)
    t.circle(15, 90)
    t.end_fill()
    

    
tela.onscreenclick(desenhar_maça)

turtle.done()