import turtle
import time
import os






# GAME VARIABLES
FPS = 0.01
score_a = 0
score_b = 0


# Screen
screen = turtle.Screen()
screen.title('Pong - CodeWithAaqid')
screen.bgcolor('green')
screen.setup(width=800, height=600)
screen.tracer(0)


# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed(0)
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


# paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.color('white')
paddle_a.speed(0)
paddle_a.goto(-350,0)
paddle_a_dy = 30

# paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.color('white')
paddle_b.speed(0)
paddle_b.goto(350,0)
paddle_b_dy = 30



# score_writer
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color('white')
score_writer.goto(0,250)
score_writer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold'), align='Center')


# moving the paddle up
def paddle_a_up():
	if paddle_a.ycor() + 50 < 300:
		paddle_a.sety(paddle_a.ycor() + paddle_a_dy)

def paddle_a_down():
	if paddle_a.ycor() - 50 > -300:
		paddle_a.sety(paddle_a.ycor() - paddle_a_dy)

def paddle_b_up():
	if paddle_b.ycor() + 50 < 300:
		paddle_b.sety(paddle_b.ycor() + paddle_b_dy)

def paddle_b_down():
	if paddle_b.ycor() - 50 > -300:
		paddle_b.sety(paddle_b.ycor() - paddle_b_dy)


screen.listen()
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')



while True:
	

	# Moving the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)



	# Top and bottom collison
	if ball.ycor() > 290:
		ball.dy *= -1
		os.system('aplay ./Sounds/bounce.wav &')
	elif ball.ycor() < -290:
		ball.dy *= -1
		os.system('aplay ./Sounds/bounce.wav &')


	# Left and right logic
	if ball.xcor() > 390:
		ball.dx *= -1
		ball.goto(0,0)
		score_a += 1
		score_writer.clear()
		score_writer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold'), align='Center')
		os.system('aplay ./Sounds/respawn.wav &')
	elif ball.xcor() < -390:
		ball.dx *= -1
		ball.goto(0,0)
		score_b += 1
		score_writer.clear()
		score_writer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold'), align='Center')
		os.system('aplay ./Sounds/respawn.wav &')
		


	# paddle and ball collisons
	if ball.xcor() < paddle_a.xcor() + 20 and ball.ycor() < paddle_a.ycor() + 65 and ball.ycor() > paddle_a.ycor() - 65:
		ball.dx *= -1
		os.system('aplay ./Sounds/bounce.wav &')

	elif ball.xcor() > paddle_b.xcor() - 20 and ball.ycor() < paddle_b.ycor() + 65 and ball.ycor() > paddle_b.ycor() - 65:
		ball.dx *= -1
		os.system('aplay ./Sounds/bounce.wav &')

	# Update the frame
	screen.update()
	time.sleep(FPS)