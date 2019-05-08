#First pygame

import pygame, sys
pygame.init()
import time

#variables
FPS = 30
WINDOW_SIZE = (1000,700)
fps_clock = pygame.time.Clock()\
#SCORE = 0

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (240, 255, 44)
SKY_BLUE = (139, 168, 194)
ORANGE = (255, 101, 0)
TAN = (247, 170, 115)
BROWN = (116, 55, 6)
LIGHT_GREEN = (107, 255, 107)
DARK_GREEN = (0, 100, 0)
DARKER_TAN = (252, 152, 80)

#x and y variables
x = 0
y = 0
second_x = 0
second_y = 0
third_x = 0
third_y = 0

#set up window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('My Game')

#drawing defs
def draw_character(x, y):
	#drawing character
	pygame.draw.circle(screen, TAN, (x + 50, y + 550), 10)
	pygame.draw.rect(screen, RED, (x + 40, y + 540, 20, 5))
	pygame.draw.rect(screen, RED, (x + 42, y + 535, 10, 8))
	pygame.draw.line(screen, BLACK, (x + 48, y + 546), (x + 48, y + 551), 2)
	pygame.draw.line(screen, BLACK, (x + 50, y + 558), (x + 55, y + 553))
	pygame.draw.line(screen, BLACK, (x + 55, y + 553), (x + 60, y + 550))
	pygame.draw.line(screen, BLACK, (x + 50, y + 553), (x + 55, y + 550), 3)
	pygame.draw.line(screen, BLACK, (x + 55, y + 550), (x + 60, y + 548), 3)
	pygame.draw.rect(screen, BLACK, (x + 40, y + 545, 3, 6))
	pygame.draw.circle(screen, BLUE, (x + 50, y + 570), 10)
	pygame.draw.rect(screen, RED, (x + 40, y + 570, 20, 10))
	pygame.draw.rect(screen, RED, (x + 42, y + 580, 5, 10))
	pygame.draw.rect(screen, RED, (x + 53, y + 580, 5, 10))
	pygame.draw.rect(screen, BLUE, (x + 41, y + 590, 8, 5))
	pygame.draw.rect(screen, BLUE, (x + 53, y + 590, 8, 5))
	pygame.draw.line(screen, BLUE, (x + 43, y + 565), (x + 34, y + 580), 5)
	pygame.draw.line(screen, BLUE, (x + 56, y + 565), (x + 64, y + 580), 5)
	pygame.draw.circle(screen, TAN, (x + 34, y + 582), 5)
	pygame.draw.circle(screen, TAN, (x + 64, y + 582), 5)

def draw_ground(second_x, second_y):	
	#drawing the ground
	pygame.draw.rect(screen, BROWN, (second_x - 100000, second_y + 595, 1000000, 1000000))
	pygame.draw.rect (screen, DARK_GREEN, (second_x - 100000, second_y + 595, 1000000, 5))

def draw_box(x, y):
	hitbox = pygame.draw.rect(screen, BLACK, (x + 29, y + 535, 40, 60), 1)
	return hitbox
	
def draw_coin(second_x, second_y):
	pygame.draw.circle(screen, YELLOW, (second_x + 500, second_y + 350), 20)
	pygame.draw.circle(screen, BLACK, (second_x + 500, second_y + 350), 10, 1)

def draw_hitbox(second_x, second_y):
	coin_hitbox = pygame.draw.circle(screen, BLACK, (second_x + 500, second_y + 350), 20, 1)
	return coin_hitbox
	
def draw_pipe(second_x, second_y):
	pygame.draw.rect(screen, GREEN, (second_x + 464, second_y + 515, 72, 80))
	pygame.draw.rect(screen, DARK_GREEN, (second_x + 464, second_y + 515, 1, 80))
	pygame.draw.rect(screen, LIGHT_GREEN, (second_x + 534, second_y + 515, 1, 80))
	pygame.draw.rect(screen, GREEN, (second_x + 459, second_y + 490, 82, 25))
	pygame.draw.rect(screen, BLACK, (second_x + 459, second_y + 490, 82, 25), 1)
	pygame.draw.line(screen, BLACK, (second_x + 459, second_y + 490), (second_x + 541, second_y + 490), 2)

def draw_cube(second_x, second_y):
	pygame.draw.rect(screen, DARKER_TAN, (second_x + 200, second_y + 450, 36, 36))
	pygame.draw.rect(screen, BROWN, (second_x + 200, second_y + 450, 36, 36), 1)
	pygame.draw.line(screen, WHITE, (second_x + 209, second_y + 455), (second_x + 226, second_y + 455), 5)
	pygame.draw.line(screen, WHITE, (second_x + 226, second_y + 455), (second_x + 226, second_y + 465), 5)
	pygame.draw.line(screen, WHITE, (second_x + 226, second_y + 465), (second_x + 210, second_y + 465), 5)
	pygame.draw.line(screen, WHITE, (second_x + 212, second_y + 465), (second_x + 212, second_y + 475), 5)
	pygame.draw.circle(screen, WHITE, (second_x + 212, second_y + 480), 2)

def draw_cloud(third_x, third_y):
	pygame.draw.circle(screen, WHITE, (third_x + 200, third_y + 200), 50)
	pygame.draw.circle(screen, WHITE, (third_x + 250, third_y + 200), 50)
	pygame.draw.circle(screen, WHITE, (third_x + 300, third_y + 200), 50)
	pygame.draw.circle(screen, WHITE, (third_x + 350, third_y + 200), 50)

#write text
my_font = pygame.font.Font('freesansbold.ttf', 48)
text = my_font.render('SCORE: 00', True, BLACK)
text_rect = text.get_rect()
text_rect.center = (150, 50)

#game loop
while True:
	#draw stuff here
	screen.fill(SKY_BLUE)
	draw_coin(second_x, second_y)
	draw_character(x + 398, y)
	draw_pipe(second_x, second_y)
	draw_cube(second_x, second_y)
	draw_cube(second_x + 35, second_y)
	draw_cloud(third_x, third_y)
	draw_cloud(third_x + 500, third_y)
	#draw_box(x, y)
	draw_ground(second_x, second_y)
	screen.blit(text, text_rect)
	
	#defining the functions
	keystate = pygame.key.get_pressed()
	
	#calling the functions
	if keystate[pygame.K_RIGHT]:
		second_x += -5
		if keystate[pygame.K_RETURN]:
			second_x += -10
	elif keystate[pygame.K_LEFT]:
		second_x += 5
		if keystate[pygame.K_RETURN]:
			second_x += 10
	#elif keystate[pygame.K_UP]:
		#y += -5
	#if keystate[pygame.K_SPACE]:
		#second_y += 50
	if second_y>25:
		second_y += -25
	elif second_y==25:
		second_y += -25
	elif second_y==24:
		second_y+= -24
	elif second_y==23:
		second_y+= -23
	elif second_y==22:
		second_y += -22
	elif second_y==21:
		second_y+= -21
	elif second_y==20:
		second_y+= -20
	elif second_y==19:
		second_y += -19
	elif second_y==18:
		second_y+= -18
	elif second_y==17:
		second_y+= -17
	elif second_y==16:
		second_y += -16
	elif second_y==15:
		second_y+= -15
	elif second_y==14:
		second_y+= -14
	elif second_y==13:
		second_y += -13
	elif second_y==12:
		second_y+= -12
	elif second_y==11:
		second_y+= -11
	elif second_y==10:
		second_y += -10
	elif second_y==9:
		second_y+= -9
	elif second_y==8:
		second_y+= -8
	elif second_y==7:
		second_y += -7
	elif second_y==6:
		second_y+= -6
	elif second_y==5:
		second_y+= -5
	elif second_y==4:
		second_y += -4
	elif second_y==3:
		second_y+= -3
	elif second_y==2:
		second_y+= -2
	elif second_y==1:
		second_y+= -1
	elif second_y==0:
		second_y+=0
		if keystate[pygame.K_SPACE]:
			second_y += 250
	
	if second_x<0 and second_x>-102:
		second_y=105
		if keystate[pygame.K_SPACE]:
			second_y += 150
	elif second_x>165 and second_x<256:
		second_y=145
		if keystate[pygame.K_SPACE]:
			second_y += 150
	#if draw_box(x + 398, y).colliderect(draw_hitbox(second_x, second_y)):
		#pygame.draw.circle(screen, SKY_BLUE, (second_x + 500, second_y + 350), 20)
			
	#print (x)
	#print (y)
	print (second_x)
	print (second_y)
	
	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#refresh the screen
	pygame.display.update()
	fps_clock.tick(FPS)
