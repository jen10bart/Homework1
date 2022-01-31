import turtle
wn=turtle.Screen()
ed=turtle.Turtle()

ed.speed('fastest')
ed.pencolor('blue')
square=int(input("How many squares to draw?: "))
units=int(input("What unit to increment the length of each side of the square?: "))


for i in range(square*5):
    ed.forward(30)
    ed.right(1000)
    units=10+units
    ed.forward(units)
   
