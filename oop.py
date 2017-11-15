class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorite_color=favorite_color
		
	def eat(self,food):
		print("Yummy!"+self.name+" is eating "+food)
	def description(self):
		print(self.name+" is "+ str(self.age) +" years old and loves the color "+ self.favorite_color)
	def make_sound(self):
		print(self.sound *3)


lion =Animal('roarrr ',"simba",7,"black")
lion.eat("meet")
lion.description()
lion.make_sound()


class Person(object):
	def __init__(self,name,age,city,gender,eye_color,favorite_food,favorite_activity):
	   self.name=name
	   self.age=age
	   self.city=city
	   self.gender=gender
	   self.eye_color=eye_color
	   self.favorite_food=favorite_food
	   self.favorite_activity=favorite_activity

	def eat_favorite_food(self):
	  	print(" her favorite food is " + self.favorite_food)
	def breathing(self):
		print(" shiki likes "+ str(self.favorite_activity))


shiki = Person("shiki",14,"Modi'in","female","brown","avocado","breathing")
shiki.eat_favorite_food()
shiki.breathing()


