from turtle import *
import turtle
import time
import random
from ball import *
colormode(255)
tracer(0)
hideturtle()

getscreen().setup(1.0, 1.0)

SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

bgcolor("black")
running = True
sleep = 0.0077
number_of_BALLS = 7
minimum_ball_radius = 3
maximum_ball_radius = 60
minimum_ball_dx = -3
maximum_ball_dx = 3
minimum_ball_dy = -3
maximum_ball_dy = 3



balls =[]

MY_BALL = Ball(0,0,0,0,25,"red")

# life_counter=3




for i in range(number_of_BALLS):

	screen_random1_x = int(-screen_width+maximum_ball_radius)
	screen_random2_x = int(screen_width-maximum_ball_radius)
	random_x = random.randint(screen_random1_x,screen_random2_x)
	
	
	screen_random1_y = int(-screen_height+maximum_ball_radius)
	screen_random2_y = int(screen_height-maximum_ball_radius)
	random_y = random.randint(screen_random1_y,screen_random2_y)

	random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while random_dx == 0:
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

	random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while random_dy == 0:
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	radius = random.randint(minimum_ball_radius,maximum_ball_radius)


	while random_x-radius<100 and random_x+radius>-100 and random_y-radius <100 and random_y+radius>-100:
			random_x = random.randint(screen_random1_x,screen_random2_x)
			random_y = random.randint(screen_random1_y,screen_random2_y)
			
	print("y: "+str(random_y))
	print("x:"+str(random_x))
		    
	

	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	


	ball = Ball(random_x,random_y,random_dx,random_dy,radius,color)
	balls.append(ball)

turtle.color("white")
turtle.write("3", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()
turtle.write("2", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()
turtle.write("1", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()


score  = 0

def move_all_balls():
	for variable in range(number_of_BALLS):
		balls[variable].move(screen_width,screen_height)

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

						
	balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5

	if balls_distance <= ball_a.r+ball_b.r:
		return True
	else:
		return False



def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if check_collide(ball_a,ball_b) == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				random_x = random.randint(screen_random1_x,screen_random2_x)

				random_y = random.randint(screen_random1_y,screen_random2_y)

				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				radius = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
								

				if radius1 > radius2:
					ball_b.goto(random_x,random_y)
					ball_b.x = random_x
					ball_b.y = random_y
					ball_b.dx = random_dx
					ball_b.dy = random_dy
					ball_b.r = radius
					ball_b.color(color, color)
					ball_a.r+= 1 
					ball_b.shapesize(ball_b.r/10)
					ball_a.shapesize(ball_a.r/10)
	
					
				elif radius1 < radius2:
					ball_a.goto(random_x,random_y)
					ball_a.x = random_x
					ball_a.y = random_y
					ball_a.dx = random_dx
					ball_a.dy = random_dy
					ball_a.r = radius

					ball_a.color(color, color)
					ball_b.r += 1
					ball_a.shapesize(ball_a.r / 10)
					ball_b.shapesize(ball_b.r/10)
					



def check_myball_collision():			
	for ball in balls:
		random_x = random.randint(screen_random1_x,screen_random2_x)
		random_y = random.randint(screen_random1_y,screen_random2_y)

		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		







		if check_collide(MY_BALL,ball):
			new_radius = MY_BALL.r
			new_radius2 = ball.r
			
			if MY_BALL.r < ball.r:
				return False
			else:
				MY_BALL.r =new_radius + 1
				global score
				score+=1
				clear()
				pu()
				turtle.goto(-500,250)
				write(score,align='center',font=('Arial',48,'normal'))
				MY_BALL.shapesize(MY_BALL.r/10)
				print(MY_BALL.r)
				ball.goto(random_x,random_y)
				ball.x = random_x
				ball.y = random_y
				ball.dx = random_dx
				ball.dy = random_dy
				ball.r = radius
				ball.color(color, color)
				ball.shapesize(ball.r/10)
	return True


def movearound(event):
	MY_BALL.goto(event.x-screen_width,screen_height-event.y)
turtle.getcanvas().bind("<Motion>", movearound)
getscreen().listen()


# def timer():
# 	timer.goto(350,200)
# 	i=60
# 	while i>-1:
# 		i=i-1
# 		time.sleep(1)
# 		time.clear()
# 		time.write("Time: ", move=False, align="center", font=("Arial", 50, "bold"))


temp = MY_BALL.r


while running == True:
    if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
        screen_width =int(turtle.getcanvas().winfo_width()/2)
        screen_height = int(turtle.getcanvas().winfo_height()/2)

    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(screen_width,screen_height)
    running=check_myball_collision()
    

    turtle.color("white")
    
    if  temp > MY_BALL.r:
    	score+=1
    	temp = MY_BALL.r
    	print ("yay!")
    	turtle.write(score, move=False, align="left", font=("Arial", 50, "bold"))




    if running == False:
    	turtle.color(255,255,255)
    	pu()
    	turtle.goto(0,0)
    	turtle.write("Game Over!", move=False, align="center", font=("Arial", 50, "bold"))
    	
    if running== False:
    	turtle.color(255,255,255)
    	pu()
    	turtle.goto(0,-75)
    	turtle.write(score, move=False, align="left", font=("Arial", 50, "bold"))



    	


    
   
    turtle.color('white')

    if score==10:
    	turtle.color(255,255,255)
    	pu()
    	turtle.goto(0,0)
    	turtle.write("You Won!!", move=False, align="center", font=("Arial", 50, "bold"))
    	
    	time.sleep(10)
    	quit()

    if score==10:
    	turtle.color(255,255,255)
    	pu()
    	turtle.goto(-200,-200)
    	turtle.write(score, move=False, align="left", font=("Arial", 50, "bold"))

    	time.sleep(10)
    	quit()


		
    





   
    getscreen().update()
    time.sleep(sleep)


mainloop()