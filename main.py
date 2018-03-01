#!/usr/bin/python

import pygame, sys, time
import serial
from pygame.locals import *
import math, random
from colors import *
import player
import arrow

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
	textSurfaceObj = fontObj.render(strg,True, RED,BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (WIDTH/2, 60)
	surf.blit(textSurfaceObj,textRectObj)
	pygame.display.update()
	time.sleep(1)

def main():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((1200,600)) #main window
	pygame.display.set_caption('Duel Game')
	#s = serial.Serial("/dev/ttyACM0") #serial connection
	FPS = 30 #frames/s
	fpsClock = pygame.time.Clock()
	player1 = player.Player(10,HEIGHT/2,GREEN)
	player2 = player.Player(WIDTH-10,HEIGHT/2,RED)
	P1_arrows = []
	P2_arrows = []
	objs = [player1,player2]

	#main game loop
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					player1.movePlayer(0,-20)
				if event.key == pygame.K_s:
					player1.movePlayer(0,20)
				if event.key == pygame.K_a:
					player1.movePlayer(-20,0)
				if event.key == pygame.K_d:
					player1.movePlayer(20,0)
				if event.key == pygame.K_UP:
					#move player up
					player2.movePlayer(0,-20)
				if event.key == pygame.K_DOWN:
					#move player down
					player2.movePlayer(0,20)
				if event.key == pygame.K_LEFT:
					#move player left
					player2.movePlayer(-20,0)
				if event.key == pygame.K_RIGHT:
					#move player right
					player2.movePlayer(20,0)
				if (event.key == pygame.K_SPACE):
					#fire arrow
					newarrow2 = arrow.Arrow(player2.x,player2.y,2)
					objs.append(newarrow2) #add arrow to objs
					player2.fire(newarrow2)
					P2_arrows.append(newarrow2)
				if (event.key == pygame.K_c):
					newarrow1 = arrow.Arrow(player1.x,player1.y,1)
					objs.append(newarrow1)
					player1.fire(newarrow1)
					P1_arrows.append(newarrow1)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		draw_world(DISPLAYSURF) #draw background
		if P1_arrows:
			for item in P1_arrows:
				item.move(1.0/FPS) #update P1 arrows if there are any
				if (player2.hitBy(item)):
					displayText("HIT!",DISPLAYSURF)
		if P2_arrows:
			for item in P2_arrows:
				item.move(1.0/FPS)
				if (player1.hitBy(item)):
					displayText("HIT!",DISPLAYSURF)
		fpsClock.tick(FPS)
		#s.write('p') #send cmd to send serial data
		#x = s.readline() #read from potentiometers
		#pot = x.rstrip().split(",") #split up values
		#Launcher1.changeAngle(pot[0]/10.0) #change angle (scaled)
		#Launcher1.changeMagnitude(pot[1]/10.0) #change magnitude (scaled)
		for obj in objs:
			obj.draw(DISPLAYSURF) #draw objects
		pygame.display.update()



if __name__=="__main__":
	main()
