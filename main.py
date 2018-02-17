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
	pygame.draw.rect(surf,SKY_COLOR,(0,0,WIDTH,HEIGHT)) #background
	pygame.draw.line(surf,RED,(WIDTH/2,0),(WIDTH/2,HEIGHT),10)#draw boundary line
	#pygame.draw.rect(surf,(GRASS_COLOR),(0,380,500,20)) #grass
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
pygame.display.set_caption('Launcher')
#s = serial.Serial("/dev/ttyACM0") #serial connection
FPS = 30 #frames/s
fpsClock = pygame.time.Clock()

player1 = player.Player(10,HEIGHT/2)
player2 = player.Player(WIDTH-10,HEIGHT/2)
arrow1 = Arrow.arrow(10,HEIGHT/2)
objs = [player1,player2,arrow1]

while(True):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP: 
				#move player up
				player1.movePlayer(-5,0)
			if event.key == pygame.K_DOWN: 
				#move player down
				player1.movePlayer(5,0)
			if event.key == pygame.K_LEFT:
				#move player left
				player1.movePlayer(0,-5)
			if event.key == pygame.K_RIGHT:
				#move player right
				player1.movePlayer(0,5)
			if (event.key == pygame.K_SPACE)
				#fire arrow
				player1.fire(arrow1)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	draw_world(DISPLAYSURF) #draw background
	pygame.display.update()
	fpsClock.tick(FPS)
	#x = s.readline() #read from potentiometers
	#pot = x.rstrip().split(",") #split up values
	#Launcher1.changeAngle(pot[0]/10.0) #change angle (scaled)
	#Launcher1.changeMagnitude(pot[1]/10.0) #change magnitude (scaled)
	for obj in objs:
		obj.draw(DISPLAYSURF) #draw objects

	









