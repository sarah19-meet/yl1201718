from turtle import *
import random
import math

class Rectangle(Turtle):
	def __init__(self,width,hight):
		Turtle.__init__(self)
		register_shape("rec",((width,0),(width,hight),(0,hight),(0,0)))
		self.shape("rec")
		self.shapesize()




rec1=Rectangle(20,40)
rec2=Rectangle(50,100)
rec1.pu()
rec2.pu()


A=1
B=2

A.top()=(rec1.ycor())+self hight/2
A.bot()=(rec1.ycor())-self hight/2
A.right()=(rec1.xcor())+self width/2
A.left()=(rec1.xcor())-self width/2

B.top()=(rec2.ycor())-self hight/2
B.bot()=(rec2.ycor())+self hight/2
B.right()=(rec2.xcor())-self width/2
B.left()=(rec2.xcor())+self width/2
 




def check_collision():

	if A.top()>B.bot() and A.right()>B.left() and A.bot<B.top() and A.left()<B.right():

		return collision



check_collision()
mainloop()

