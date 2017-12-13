from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)

def checkCollision(ball,ball2):
    global x1 
    global x2 
    global y1
    global y2
    global r1
    global r2


ball= Ball(100,"black",1)
ball2=Ball(50,"green",1)
ball.pu()
ball2.pu()


ball.goto(50,50)
ball2.goto(-50,-50)


x1=ball.xcor()
x2=ball2.xcor()
y1=ball.ycor()
y2=ball2.ycor()
r1=ball.radius 
r2=ball2.radius

global d
d=d=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

if (d < r1 + r2):
	ball.color("red")
	ball2.color("yellow")







checkCollision(ball,ball2)

def Collision():
	if (d<r1 + r2):
		print("Collision")
		if r1 >r2:
			y = random.randint(-50,200) 
			x = random.randint(-50,200)
			ball2.goto(x,y)
		else:
			y = random.randint(-50,200) 
			x = random.randint(-50,200)
			ball1.goto(x,y)






Collision()

mainloop()
