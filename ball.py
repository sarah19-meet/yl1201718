from turtle import *
import turtle

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		turtle.pu()
		self.dx = dx
		self.pu()
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.goto(x,y)
		self.color(color)
		self.shape("circle")


	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + dx 
		current_y = self.ycor()
		new_y = current_y + dy
		right_side_ball = new_x + r
		left_side_ball = new_x - r
		top_side_ball = new_y + r
		bottom_side_ball = new_y - r
		self.goto(new_x,new_y)

		if top_side_ball > 300:
			new_y = current_y - dy

		elif bottom_side_ball < -300:
			new_y = current_y + dy

		elif left_side_ball < -300:
			new_x = current_x + dx

		elif right_side_ball > 300:
			new_x = current_x - dx