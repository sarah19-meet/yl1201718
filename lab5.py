from turtle import *
import random
colormode(255)
class Square(Turtle):
	def __init__ (self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize()



	def random_color(self):
		r=random.randint(0,256)
		g=random.randint(0,256)
		b=random.randint(0,256)
		self.color((r,g,b))

square1=Square(7)
square1.random_color()

class Rectangle(Turtle):
	def __init__(self,width,hight):
		Turtle.__init__(self)
		register_shape("rec",((width,0),(width,hight),(0,hight),(0,0)))
		self.shape("rec")
		self.shapesize()

Rectangle1=Rectangle(20,40)

class Square1(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)

new_square= Square1(40)

class Polygon(Turtle):












mainloop()
