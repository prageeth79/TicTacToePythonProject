#####################################################################################################
#	TIC TAC TOE THE GAME YOU LOVED
#----------------------------------------------------------------------------------------------------
#	this is the game tic tac toe the game you were playing as children is is fully funcitonal
#   with the capability of AI you can draw with it and have fun enjoy!
#	P.S. this program required pygame along side with python 3 to work install pygame 
#	to your python 3 (e.g. C:\>pip install pygame) to make it work.
#----------------------------------------------------------------------------------------------------
#	Copyright (C) Prageeth Niranjan 2019
#	Version 1.0.0
#----------------------------------------------------------------------------------------------------
# HOW TO RUN: copy the code in this page and paste it on a text editor and name the file as tic_tac_toe.py 
# then use command prompt to run c:\<dir path>\python tic_tac_toe.py
#####################################################################################################

import pygame, random, sys, os, math, random
from enum import Enum

# width and hight of the screen
WIDTH = 400
HEIGHT = 400

# the game array
tic_tac_toe = [0, 0, 0, 0, 0, 0, 0, 0, 0]	

# shift of player and compuer X and O
x_shift = 40

# score assined to the board
game_score = 1
player_score = game_score
computer_score = -game_score

# disply text position
text_x = 50
text_y = int(HEIGHT / 2 - 10)

#values use for X and O
CHARACTOR_FOR_X = 'x'
CHARACTOR_FOR_O = 'o'

#define the Players
_player = CHARACTOR_FOR_X
_computer = CHARACTOR_FOR_O

# First turn Player or computer
turn = _player

# Collors to be used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW =  (255,255,0)
DISPLAY_MESSAGE_HEIGHT = 150
DISPLAY_MESSAGE_ALPHA = 200

BACKGROUND_COLOR = BLACK 								# this varialbe set's the background color

screen = ""
myFont = ""
m_display = ""

gameOver = False

def init_pygame(): 										# this function initialize the pygame

	global screen, myFont, m_display

	pygame.init()										# initilze pygame

	pygame.display.set_caption('TIC TAC TOE') 			# set pygame caption
	
	myFont = pygame.font.SysFont('monospace', 30)		# get the font 'monospace' with size 30

	screen = pygame.display.set_mode((WIDTH, HEIGHT))   # set the display windows width and height

	pygame.display.update()								# update the display window

	m_display = pygame.Surface((WIDTH,DISPLAY_MESSAGE_HEIGHT))				# make the message background
	m_display.set_alpha(DISPLAY_MESSAGE_ALPHA)							# make the message background transparent
	m_display.fill(BLACK)								# fill message background with black

def game_screen(COLOR): 								# this is a function to draw the grid line of screen and the moves made
	global screen, tic_tac_toe
	pygame.draw.line(screen, COLOR, (int(WIDTH / 3),0), (int(WIDTH / 3),HEIGHT), 2)
	pygame.draw.line(screen, COLOR, (int(2 * WIDTH / 3),0), (int(2 * WIDTH / 3),HEIGHT), 2)
	pygame.draw.line(screen, COLOR, (0,int(HEIGHT / 3)), (WIDTH,int(HEIGHT/3)), 2)
	pygame.draw.line(screen, COLOR, (0,int(2 * HEIGHT / 3)), (WIDTH,int(2 * HEIGHT / 3)), 2)

	for i in range(0, 9):								# draw the player posision
		if tic_tac_toe[i] == player_score:
			draw_charactor(i,BLUE,_player)
	for i in range(0, 9):								# draw the computer posision
		if tic_tac_toe[i] == computer_score:
			draw_charactor(i,BLUE,_computer)

def find_pos(pos):										# find the mouse position related to the grid
	#pos = pygame.mouse.get_pos()	
	x = pos[0] // (WIDTH / 3)
	y = pos[1] // (HEIGHT / 3)
	return int(y * 3 + x )
	
def drawX(pos, COLOR):									# draw the X in the grid
	global screen
	x = pos % 3
	y = pos // 3

	xi = math.ceil(x * WIDTH / 3 )
	yi = math.ceil( y * HEIGHT / 3 )
	pygame.draw.line(screen, COLOR, (int(xi + x_shift), int(yi + x_shift)), (int(xi + WIDTH/3 - x_shift), int(yi + HEIGHT/3 -  x_shift)), 10)
	pygame.draw.line(screen, COLOR, (int(xi + x_shift), int(yi + HEIGHT / 3 - x_shift)), (int(xi + WIDTH / 3 -  x_shift),  int(yi +  x_shift)), 10)

def drawO(pos, COLOR):									# draw the O in the grid
	global screen
	x = pos % 3
	y = pos // 3    

	xi = math.ceil( x * WIDTH / 3 + WIDTH / 6 )
	yi = math.ceil( y * HEIGHT / 3 + HEIGHT / 6 )
	pygame.draw.circle(screen,COLOR,(xi,yi), math.ceil(WIDTH / 6 - x_shift), 10)
    
def draw_charactor(pos,COLOR, charactor): 				# this function draws X or O depending of choice
    if charactor == CHARACTOR_FOR_X:
        drawX(pos,COLOR)
    elif charactor == CHARACTOR_FOR_O:
        drawO(pos,COLOR)

def process_input():									# process the input of the system
	global tic_tac_toe, turn, gameOver
	# this handle the keyboard & mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 					# if press quit
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1: # if left mouse button is pressed
			if turn == _player and not gameOver:			# if it is the players turn do this
				tic_tac_toe[find_pos(event.dict['pos'])] = player_score				
				turn = _computer

def computer_move(x_a):									# this function handle the AI 

	for val in  [2 * computer_score, 2 * player_score]: # -2 check for winning conditon and 2 for blocking the win of player
		if x_a[0] + x_a[4] + x_a[8] == val:				# check diaganaly /
			if x_a[0] == 0:
				return 0
			elif x_a[4] == 0:
				return 4
			elif x_a[8] == 0:				
				return 8

		if x_a[2] + x_a[4] + x_a[6] == val:				# check diaganaly \
			if x_a[2] == 0:
				return 2
			elif x_a[4] == 0:
				return 4
			elif x_a[6] == 0:
				return 6

		for i in [0, 3, 6]:
			if x_a[i] + x_a[i+1] + x_a[i+2] == val:		# check Horizontaly
				if x_a[i] == 0:
					return i
				elif x_a[i+1] == 0:
					return i+1
				elif x_a[i+2] == 0:
					return i+2

		for i in [0, 1, 2]:
			if x_a[i] + x_a[i+3] + x_a[i+6] == val:		# check vertically
				if x_a[i] == 0:
					return i
				elif x_a[i + 3] == 0:
					return i + 3
				elif x_a[i + 6] == 0:
					return i + 6

	while not no_moves():								# if no wining or blocking situation make a random move
		pos = random.randint(0,89) // 10		
		if x_a[pos] == 0:								# if the posision is empty
			return pos


def no_moves():											# to find out any moves left
	global tic_tac_toe
	for i in range(0, 9):
		if tic_tac_toe[i] == 0:							# if the posision is empty
			return False
	return True

def win(x_a,player):									# find the winner
	global player_score, computer_score
	if player == _player:
		score = player_score * 3
	else:
		score = computer_score * 3

	if x_a[0] + x_a[4] + x_a[8] == score or x_a[2] + x_a[4] + x_a[6] == score or \
	x_a[0] + x_a[1] + x_a[2] == score or x_a[3] + x_a[4] + x_a[5] == score or x_a[6] + x_a[7] + x_a[8] == score or \
	x_a[0] + x_a[3] + x_a[6] == score or x_a[1] + x_a[4] + x_a[7] == score or x_a[2] + x_a[5] + x_a[8] == score:		# check if there is a wining situation
		return True
	else:
		return False

def draw_win(x_a,COLOR):							   			# draw the wining lines 
	global screen
	for val in  [3 * computer_score, 3 * player_score]: 				
		if x_a[0] + x_a[4] + x_a[8] == val:
			pygame.draw.line(screen,COLOR, (0,0), (WIDTH,HEIGHT), 4)
		if x_a[2] + x_a[4] + x_a[6] == val:
			pygame.draw.line(screen,COLOR, (0,HEIGHT), (WIDTH,0), 4)
		for i,num in enumerate([0, 3, 6]):
			if x_a[num] + x_a[num+1] + x_a[num + 2] == val:
				pygame.draw.line(screen,COLOR, (0,int(i * HEIGHT / 3 + HEIGHT / 6)), (WIDTH,int(i * HEIGHT / 3 + HEIGHT / 6)), 4)
		for num in [0, 1, 2]:
			if x_a[num] + x_a[num+3] + x_a[num + 6] == val:
				pygame.draw.line(screen,COLOR, (int(num * WIDTH / 3 + WIDTH / 6),0), (int(num * WIDTH / 3 + WIDTH / 6),HEIGHT), 4)

def display_messege(message,COLOR):                     		# this function use to deiplay message (WIN) to screen	
    global screen,myFont
    screen.blit(m_display,(0, int(HEIGHT / 2 - 80)))
    wins = myFont.render(message,2,COLOR)
    screen.blit(wins, (text_x, text_y))

def game():														# main game function
	global screen, tic_tac_toe, gameOver, turn, text_x, text_y, computer_score, myFont, m_display, BLUE, GREEN, WHITE, HEIGHT, WIDTH

	init_pygame() 												# initialize the pygame settings
	# main game loop execution bigins hear
	while True:
		screen.fill(BACKGROUND_COLOR)
		process_input()
		game_screen(WHITE)
		if not gameOver:										# do this if game is not over			
			if turn == _computer and not win(tic_tac_toe,_player) and not no_moves(): #if it is the computers turn do this
				tic_tac_toe[computer_move(tic_tac_toe)] = computer_score			
				turn = _player				
			gameOver = win(tic_tac_toe, _player) or win(tic_tac_toe, _computer)		

		else:			
			draw_win(tic_tac_toe,RED)
			if win(tic_tac_toe,_player):						# if player wins show message		
				display_messege("player Wins!!!", GREEN)
			elif win(tic_tac_toe,_computer):					# if computer wins show message		
				display_messege("Computer Wins!!", GREEN)
			

		if no_moves():											# if no more moves show message
			pygame.draw.line(screen,RED,(0,0),(WIDTH,HEIGHT),4)
			pygame.draw.line(screen,RED,(0,HEIGHT),(WIDTH,0),4)		
			display_messege("No more moves!!", GREEN)
		
		pygame.display.update()


game() 															# game bigins here
