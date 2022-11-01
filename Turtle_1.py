import turtle


def triangle(turt, edge=100):
    for x in range(3):
        turt.forward(edge)
        turt.left(120)


def rectangle(turt, edge=100):
    for x in range(4):
        turt.forward(edge)
        turt.left(90)


# Triangle Drawing
hexagon = turtle.Turtle()

for x in range(6):
    triangle(hexagon)
    hexagon.left(60)

hexagon.clear()
hexagon.hideturtle()

# Mouse Drawing

tri = turtle.Turtle()
tri.color('red')

rect = turtle.Turtle()
rect.color('blue')

eye1 = turtle.Turtle()
eye1.color('black')
eye2 = turtle.Turtle()
eye2.color('black')

smile = turtle.Turtle()

ear1 = turtle.Turtle()
ear1.color('black')
ear2 = turtle.Turtle()
ear2.color('black')

# Nose
tri.penup()
tri.setpos(-20, -75)
tri.pendown()
triangle(tri, 40)
tri.hideturtle()

# Face
rect.penup()
rect.setpos(-150, -200)
rect.pendown()
rectangle(rect, 300)
rect.hideturtle()

# Eyes
eye1.penup()
eye1.setpos(-80, 10)
eye1.pendown()
eye1.circle(25)
eye1.hideturtle()

eye2.penup()
eye2.setpos(80, 10)
eye2.pendown()
eye2.circle(25)
eye2.hideturtle()


# Smile
smile.penup()
smile.setpos(-60, -120)
smile.right(90)
smile.pendown()
smile.circle(60, 180)
smile.hideturtle()

# Ears
ear1.penup()
ear1.setpos(-150, 100)
ear1.pendown()
ear1.circle(50)
ear1.circle(75)
ear1.hideturtle()

ear2.penup()
ear2.setpos(150, 100)
ear2.pendown()
ear2.circle(50)
ear2.circle(75)
ear2.hideturtle()

turtle.exitonclick()
