import pygame
from colors import *

ARROW_LENGTH = 10
ARROW_HEIGHT = 3

class Arrow:
	def __init__(self,x,y,playernum):
		self.x = x
		self.y = y
		self.v_x = 0
		self.r = pygame.Rect(0,0,ARROW_LENGTH,ARROW_HEIGHT)
		self.r.center = (self.x,self.y)
		if playernum==1:
			self.color = GREEN
		else:
			self.color = RED

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
		pygame.draw.rect(surf,self.color, self.r)
