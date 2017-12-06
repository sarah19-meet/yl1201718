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

ball= Ball(7,"red",70)
ball2=Ball(10,"blue",50)

x1=ball.xcor()
x2=ball2.xcor()
y1=ball.ycor()
y2=ball2.ycor()




def check_collision(Ball,Ball2):
	d=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
	if d ==0:
		print("the balls  collide")

mainloop()
