from turtle import *
import turtle
import random
from ball import Ball
hideturtle()
tracer(0)

#sqrt ( x2-x1 square ) + ( y2-y1 square)
RUNNING= True
SLEEP= 0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()//2
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS =100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

	dy=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	r =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))






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




def move_all_balls():
	for ball in BALLS:
		ball.move()
		

#		def top(self):
#			return self.ycor() + (0.5 *self.height)
#		def bottom(self):
#			return self.ycor() - (0.5 * self.height)
#		def right(self):
#			return self.xcor() + (0.5 *self.width)
#		def left(self):
#			return self.xcor() - (0.5 *self.width)

#if a.top > b.bottom &
#a.right > b. right &
#a. bottom < b .bottom &
#a.left < b.left :
#return true 



my_ball = Ball(100,0,5,5,10,"red")
my_ball.goto(10,10)



BALLS.append(my_ball)


update()
mainloop()