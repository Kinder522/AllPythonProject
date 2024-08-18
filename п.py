from turtle import *
from random import randint

f = 200

def d(t):
  t.showturtle()
  t.speed(15)
  t.goto(-20, 50)
  t.write("Win", font=('Arial', 13, 'bold'))
  t.goto(30, 60)
  t.stamp()
  t.penup()
  t.goto(0, -60)
  for i in range(20):
    t.fd(30)
    t.stamp()
    t.left(360/20)
  t.goto(-40, 0)
  t.pendown()
  t.color('yellow')
  for i in range(3):
    t.begin_fill()
    for i in range(5):
      t.fd(30)
      t.left(144)
    t.end_fill()
    t.penup()
    t.fd(40)
    t.pendown()
  t.hideturtle()

def s(t, x, y, color):
  t.penup()
  t.shape('turtle')
  t.color(color)
  t.goto(x, y)

def w():
  speed(10)
  penup()
  color('red')
  pensize(5)
  goto(-160, 90)
  pendown()
  goto(-160, -90)
  penup()
  goto(-190, 90)
  pendown()
  goto(190, -90)

w()
t1 = Turtle()
s(t1 ,-170, 40, 'red')
t2 = Turtle()
s(t2 ,-170, -40, 'yellow')
t3 = Turtle()
s(t3 ,-170, 0, 'blue')
t4 = Turtle()
s(t4 ,-170, -80, 'pink')

while t1.xcor() < f and t2.xcor() < f and t3.xcor() < f and t4.xcor() < f:
   t1.forward(randint(1,10))
   t2.fd(randint(1,10))
   t3.fd(randint(1,10))
   t4.fd(randint(1,10))

clear()
max_x = max(t1.xcor(), t2.xcor(), t3.xcor(), t4.xcor())
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
if t1.xcor() == max_x:
  d(t1)
if t2.xcor() == max_x:
  d(t2)
if t3.xcor() == max_x:
  d(t3)
if t4.xcor() == max_x:
  d(t4)