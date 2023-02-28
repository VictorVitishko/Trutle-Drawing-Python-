import turtle 

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(1)
t.speed(20)
t.width(7)

def move(x, y):
    t.up()
    t.goto(x, y) 
    t.down()

def square(x=0, y=0,):
    for i in range (4):
        t.forward(x+100)
        t.left(y+90)
        t.width(7)
        
def circle(radius = 50):
    num_sides = 50
    p = 3.14
    for i in range (num_sides):
        t.forward((2*radius*p) / num_sides)
        t.left(360/num_sides)

def pentagon():
    for i in range (5):
        t.forward(100)
        t.left(72)

def polygon(n):
    for i in range (n):
        t.forward(50)
        t.left(360/n)

def spiral():
    for i in range(50):
        t.forward(i)
        t.left(15)

def olympic_circle(x, y, color):
    move(x, y)
    t.width(10)
    t.color(color)
    circle()

def olympic_logo(x=0, y=0):
    olympic_circle(x, y, 'black')
    olympic_circle(x-120, y, 'blue')  
    olympic_circle(x+120, y, 'red')
    olympic_circle(x-60, y-60, 'orange')
    olympic_circle(x+60, y-60, 'green')

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(-90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def up_or_down():
    if t.isdown():
        t.up()
    else:
        t.down()

def orange():
    t.color('orange')
    t.width(7)

def red():
    t.color('red')
    t.width(7)

def grey():
    t.color('grey')
    t.width(7)

def blue():
    t.color('blue')
    t.width(7)

def yellow():
    t.color('yellow')
    t.width(7)

def green():
    t.color('green')
    t.width(7)

def brown():
    t.color('brown')
    t.width(7)

def black():
    t.color('black')
    t.width(7)

def eracer():
    t.color('white')
    t.width(60)
    
def olympic_key():
    x = t.xcor()
    y = t.ycor()
    olympic_logo(x, y)

t.screen.onkeypress(up, 'Up')
t.screen.onkeypress(down, 'Down')
t.screen.onkeypress(left, 'Left')
t.screen.onkeypress(right, 'Right')
t.screen.onkeypress(up_or_down, 'space')
t.screen.onkeypress(olympic_key, 'O')
t.screen.onkeypress(red, 'r')
t.screen.onkeypress(blue, 'b')
t.screen.onkeypress(eracer, 'e')
t.screen.onkeypress(orange, 'o')
t.screen.onkeypress(green, 'g')
t.screen.onkeypress(black, 'B')
t.screen.onkeypress(square, 's')
t.screen.onkeypress(pentagon, 'p')
t.screen.onkeypress(spiral, 'P')
t.screen.onkeypress(yellow, 'y')
t.screen.onkeypress(grey, 'G')
t.screen.onkeypress(brown, 'b + r')
t.screen.listen()
t.screen.mainloop()