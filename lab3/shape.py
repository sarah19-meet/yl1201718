import turtle

def shape():
	for i in range (360):
		turtle.speed(500)
		turtle.pu()
		turtle.home()
		turtle.right(i)
		turtle.pd()
		turtle.forward(200)
		turtle.right(45)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(50)
shape()

turtle.mainloop()

