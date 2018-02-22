#!/usr/bin/python

import pygame, sys, time
import serial
from pygame.locals import *
import math, random
from colors import *
import player, arrow

WIDTH = 1200 #pixels
HEIGHT = 600
def draw_world(surf):
	fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
	textSurfaceObj = fontObj.render('DUEL',True,BLACK,WHITE) #white text, black highlight
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (WIDTH/2,20)
	pygame.draw.rect(surf,NAVY_BLUE,(0,0,WIDTH,HEIGHT)) #background
	pygame.draw.line(surf,RED,(WIDTH/2,0),(WIDTH/2,HEIGHT),10)#draw boundary line
	surf.blit(textSurfaceObj,textRectObj) #draw title text

def displayText(strg,surf):
	fontObj = pygame.font.Font('freesansbold.ttf',32)
	textSurfaceObj = fontObj.render(strg,True, RED)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (WIDTH/2, 60)
	surf.blit(textSurfaceObj,textRectObj)
	pygame.display.update()
	time.sleep(1)

pygame.init() 
DISPLAYSURF = pygame.display.set_mode((1200,600)) #main window
pygame.display.set_caption('Duel Game')
#s = serial.Serial("/dev/ttyACM0") #serial connection
FPS = 30 #frames/s
fpsClock = pygame.time.Clock()

player1 = player.Player(10,HEIGHT/2,GREEN)
player2 = player.Player(WIDTH-10,HEIGHT/2,RED)
objs = [player1,player2]

while(True):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP: 
				#move player up
				player1.movePlayer(0,-10)
			if event.key == pygame.K_DOWN: 
				#move player down
				player1.movePlayer(0,10)
			if event.key == pygame.K_LEFT:
				#move player left
				player1.movePlayer(-10,0)
			if event.key == pygame.K_RIGHT:
				#move player right
				player1.movePlayer(10,0)
			if (event.key == pygame.K_SPACE):
				#fire arrow
				arrow1 = arrow.Arrow(player1.x,player1.y)
				player1.fire(arrow1)
				objs.append(arrow1)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	draw_world(DISPLAYSURF) #draw background
	fpsClock.tick(FPS)
	#x = s.readline() #read from potentiometers
	#pot = x.rstrip().split(",") #split up values
	#Launcher1.changeAngle(pot[0]/10.0) #change angle (scaled)
	#Launcher1.changeMagnitude(pot[1]/10.0) #change magnitude (scaled)
	for obj in objs:
		obj.draw(DISPLAYSURF) #draw objects
	pygame.display.update()

	









