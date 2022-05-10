import pygame
import random

pygame.init()

screen = pygame.display.set_mode((720, 1134))
width, height = screen.get_size()
font = pygame.font.SysFont("", 40)

class Ball():
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
		self.yvel = 0
		self.yacc = gravity
		self.energy_loss = 2 #ball energy loss on ground collision
	def draw(self):
		pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.r)
	def move(self):
		#check if the ball is on the ground then bounce
		if self.y + self.r >= height:
			self.yvel = -(self.yvel - self.energy_loss)
		#prevents the ball from overlaping from the ground
		if (self.y + self.r) + self.yvel >= height:
			self.y = height - self.r
		else:
			self.y += self.yvel
			self.yvel += self.yacc
	#throw the ball upward equal to the value of (height - my)
	#the lower the mouse, the lower the force
	#the higher the mouse, the higher the force
	def add_yvel(self, value):
		F = (height - value) * 0.03
		self.yvel -= F

gravity = 0.5
ball_rad = 100
ball = Ball(width * 0.5, height - ball_rad, ball_rad)

def debug(antialias, font_color):
	w = font.render(f"Window width: {width}", antialias, font_color)
	h = font.render(f"Window height: {height}", antialias, font_color)
	yvel = font.render(f"Y velocity: {round(ball.yvel, 2)}", antialias, font_color)
	yacc = font.render(f"Y acceleration: {round(ball.yacc, 2)}", antialias, font_color)
	ypos = font.render(f"Y position: {round(ball.r + ball.y, 2)}", antialias, font_color)
	grav = font.render(f"Gravity: {round(gravity, 2)}", antialias, font_color)
	screen.blit(w, (0, 0))
	screen.blit(h, (0, 25))
	screen.blit(grav, (0, 50))
	screen.blit(yacc, (0, 75))
	screen.blit(yvel, (0, 100))
	screen.blit(ypos, (0, 125))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			mx, my = pygame.mouse.get_pos()
			#check if mouse is inside the ball to reset the ball
			if (mx >= ball.x - ball.r and mx <= ball.x + ball.r) and (my >= ball.y - ball.r and my <= ball.y + ball.r):
				ball.y = height - ball.r
				ball.yvel = 0
			#if not, then check if the ball is on the ground then bounce
			elif ball.y + ball.r >= height:
				ball.add_yvel(my)
	
	screen.fill((0, 0, 0))
	ball.draw()
	ball.move()
	debug(True, (255, 255, 255))
	
	pygame.display.flip()
