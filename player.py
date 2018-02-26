import pygame
import math
from colors import *


class Player:
	def __init__(self,x,y,color):
		self.x = x
		self.y = y
		self.r = pygame.Rect(0,0,30,30)
		self.color = color
		if x<600:
			self.playerside = 1
		else:
			self.playerside = 2

	def fire(self, arrow):
		arrow.v_x = 100

	def movePlayer(self,dx,dy):
		#keep players within their boundaries
		if self.playerside ==1:
			if (self.x+dx)<15 or (self.x+dx)>585:
				dx=0
			if (self.y+dy)<15 or (self.y+dy)>585:
				dy=0
		else:
			if (self.x+dx)<615 or (self.x+dx)>1185:
				dx=0
			if (self.y+dy)<15 or (self.y+dy)>585:
				dy=0
		self.x += dx
		self.y += dy

	def hitBy(self,obj):
		return self.r.colliderect(obj.r)

	def draw(self,surf):
		self.r.center = (self.x,self.y)
		pygame.draw.rect(surf,self.color,self.r)
