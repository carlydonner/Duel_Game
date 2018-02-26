import pygame
from colors import *

ARROW_LENGTH = 10
ARROW_WIDTH = 3
ARROW_SPEED = 10

class Arrow:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.r = pygame.Rect(0,0,ARROW_WIDTH,ARROW_LENGTH)
		self.r.center = (self.x,self.y)

	def move(self, dt):
		self.x += self.v_x*dt

	def moveTo(self, x, y):
		self.x = x
		self.y = y
		self.v_x = 0

	def getRect(self):
		r = pygame.Rect((0,0,ARROW_LENGTH,ARROW_WIDTH))
		r.center = (self.x, self.y)
		return r

	def isMoving(self):
		return (self.v_x!=0)

	def draw(self, surf):
		self.r.center = (self.x,self.y)
		pygame.draw.rect(surf, ARROW_COLOR, r)
