import pygame
import math
from colors import *


class Player:
	def __init__(self,x,y,color):
		self.x = x
		self.y = y
		self.angle = 45
		self.mag = 50
		self.width = 2
		self.color = color

	def fire(self, arrow):
		arrow.v_x = 50

	def movePlayer(self,dx,dy):
		self.x += dx
		self.y += dy

	def draw(self,surf):
		dx = 20
		dy = 20     
		pygame.draw.aaline(surf, self.color,
                      (self.x,self.y),
                      (self.x+dx, self.y-dy),
                       self.width)
