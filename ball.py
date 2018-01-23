from turtle import *
import turtle
import random

colormode(255)
running = True
sleep = 0.0077
screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.x = x
		self.y = y
		self.shapesize(r/10)
		self.goto(x,y)
		self.color(color)
		self.shape("circle")

	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.goto(new_x,new_y)

		if top_side_ball > height:
			self.dy = - self.dy

		elif bottom_side_ball < -height:
			self.dy = -self.dy

		elif left_side_ball < -width:
			self.dx = -self.dx

		elif right_side_ball > width:
			self.dx = -self.dx 

MY_BALL = Ball(0,0,5,5,10,"red")
