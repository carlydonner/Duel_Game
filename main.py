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
	s = serial.Serial("/dev/ttyACM0") #serial connection
	FPS = 30 #frames/s
	fpsClock = pygame.time.Clock()
	player1 = player.Player(10,HEIGHT/2,GREEN)
	player2 = player.Player(WIDTH-10,HEIGHT/2,RED)
	playerlife1 = 3
	playerlife2 = 3
	P1_arrows = []
	P2_arrows = []
	objs = [player1,player2]
	P1X = 0
	P1Y =0
	P2X = 0
	P2Y = 0

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
					player2.moveTo(WIDTH-10,HEIGHT/2)
					playerlife2 = playerlife2 -1
					if (playerlife2 < 0):
						while(1):
							displayText("BOOM! Player2 you suck! Player1 wins!",DISPLAYSURF)
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
		if P2_arrows:
			for item in P2_arrows:
				item.move(1.0/FPS)
				if (player1.hitBy(item)):
					player1.moveTo(10,HEIGHT/2)
					playerlife1 = playerlife1 -1
					if (playerlife1 < 0):
						while(1):
							displayText("BOOM! Player1 you suck! Player2 wins!",DISPLAYSURF)
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
		s.write("p") #send cmd to send serial data
		str_data = s.readline() #read from potentiometers
		data = [int(x) for x in str_data.split(',')]
		#print data
		if data[4]==1:
			newarrow1 = arrow.Arrow(player1.x,player1.y,1)
			objs.append(newarrow1)
			player1.fire(newarrow1)
			P1_arrows.append(newarrow1)
		if data[5]==1:
			newarrow2 = arrow.Arrow(player2.x,player2.y,2)
			objs.append(newarrow2) #add arrow to objs
			player2.fire(newarrow2)
			P2_arrows.append(newarrow2)
		if data[0]>518 or data[0]<512:
			P1X = -(data[0]-513.0)/10.0
		else:
			P1X=0
		if data[1]>500 or data[1]<498:
			P1Y = (data[1]-499.0)/9.0
		else:
			P1Y=0
		if data[2]>532 or data[2]<528:
			P2X = -(data[2]-530.0)/10.0
		else:
			P2X = 0
		if data[3]>515 or data[3]<512:
			P2Y = -(data[3]-513)/10.0
		else:
			P2Y = 0
		player1.movePlayer(P1X,P1Y)
		player2.movePlayer(P2X,P2Y)
		fpsClock.tick(FPS)
		for obj in objs:
			obj.draw(DISPLAYSURF) #draw objects
		pygame.display.update()



if __name__=="__main__":
	main()
