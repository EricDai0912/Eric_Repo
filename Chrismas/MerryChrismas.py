import turtle,random

def makeSnow():
    for i in range(50):
        snow=turtle.Turtle()
        snow.pu()
        snow.color("white")
        snow.shape("circle")
        snow.speed(0)
        snow.goto(random.randint(-999,999),random.randint(-999,999))
        snow.dot(7,'white')
        snowlist.append(snow)

def snowfall():
    for i in snowlist:
        i.goto(random.randint(-999,999),random.randint(-999,999))
        i.dot(7,'white')

card=turtle.Screen()
card.setup(1.0,1.0,0,0)
card.title("Merry Chrismas!")
colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
card.bgcolor(random.choice(colors))

tur=turtle.Turtle()
tur.color("green")
tur.pensize(5)
tur.begin_fill()
# Creating Right half of the tree
tur.forward(100)
tur.left(150)
tur.forward(90)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(40)
tur.left(150)
tur.forward(100)
tur.end_fill()
#left half of the tree
tur.begin_fill()
tur.left(60)
tur.forward(100)
tur.left(150)
tur.forward(40)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(90)
tur.left(150)
tur.forward(133)
tur.end_fill()
#Creating the trunck of the tree
tur.color("red")
tur.pensize(1)
tur.begin_fill()
tur.right(90)
tur.forward(80)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(80)
tur.end_fill()
#Creating the balls on the Christmas Tree
tur.penup()
tur.color("red")
tur.goto(110,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-120,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("yellow")
tur.goto(100,40)
tur.begin_fill()
tur.circle(10)
tur.end_fill()



tur.penup()
tur.color("yellow")
tur.goto(-105,38)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(85,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-95,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

#Drawing the bells using turtle.
tur.shape("triangle")
tur.fillcolor("yellow")
tur.goto(-20,30)
tur.setheading(90)
tur.stamp()
tur.fillcolor("red")
tur.goto(20,60)
tur.setheading(90)
tur.stamp()
tur.goto(-40,75)
tur.setheading(90)
tur.stamp()

# Printing the star using for loop
tur.speed(1)
tur.penup()
tur.color("yellow")
tur.goto(-20,110)
tur.begin_fill()
tur.pendown()

for i in range(5):
    tur.forward(40)
    tur.right(144)

tur.end_fill()
tur.hideturtle()

pen=turtle.Turtle()
pen.hideturtle()
pen.pu()
pen.setx(-500)
pen.write("Merry \n Chrismas!!!", font=("ravie",40,"italic"),align="center")
pen.setheading(-90)
pen.fd(100)
pen.write("To Anika \n From Eric", font=("Courier",30,"bold"),align="center")

card.tracer(False)
snowlist=[]
makeSnow()
card.tracer(True)
while True:
    snowfall()
    card.bgcolor(random.choice(colors))
pen.pu()
pen.setx(-500)
pen.write("Merry \n Chrismas!!!", font=("ravie",40,"italic"),align="center")
pen.setheading(-90)
pen.fd(100)
pen.write("To Anika", font=("Courier",30,"bold"),align="center")

card.tracer(False)
snowlist=[]
makeSnow()
card.tracer(True)
while True:
    snowfall()
    card.bgcolor(random.choice(colors))