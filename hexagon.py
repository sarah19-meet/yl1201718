class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range(6):
			self.forward(10)
			self.right(60)

		self.end_poly()
		p=self.get_poly()
		register_shape("hexagon",p)
		self.shape("hexagon")
hexagon1=Hexagon(7)