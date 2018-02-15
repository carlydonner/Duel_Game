#!/usr/bin/py

import pygame, sys, time
import serial
from pygame.locals import *
import math, random
from colors import *
#import player, arrow
import player
import arrow

WIDTH = 1200 #pixels
HEIGHT = 600
def draw_world(surf):
	pygame.draw.line(surf,RED,(WIDTH/2,0),(WIDTH/2,HEIGHT),10)#draw boundary line
	fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
	textSurfaceObj = fontObj.render('DUEL',True,BLACK,WHITE) #white text, black highlight
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (WIDTH/2,20)
	pygame.draw.rect(surf,SKY_COLOR,(0,0,WIDTH,HEIGHT)) #background
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
				#fire rock
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
"""
	if(hole1.hitBy(rock1)):
		displayText("HIT!",DISPLAYSURF)
		rock1.moveTo(0,380) #move rock back to start
		hole1.moveTo((280*random.random())+100,385) #move hole to random location
	elif(rock1.y>385):
		#send rock to start when it misses
		rock1.moveTo(0,380)
	draw_world(DISPLAYSURF) #draw background
	for obj in objs:
		obj.draw(DISPLAYSURF) #draw objects 
"""
	









