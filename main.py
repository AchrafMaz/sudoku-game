import pygame
import aa


class Cube():
	def __init__(self,pos,value = 0,color = (55,55,255)):
		self.pos = pos
		self.value = value
		self.color = color
	def get_validation(self):
		if aa.solution[self.pos[0]][self.pos[1]] == self.value:
			aa.board1[self.pos[0]][self.pos[1]] = self.value
			return True
		return False
	def draw(self,win):
		x = self.pos[1]*50
		y = self.pos[0]*62
		pygame.draw.rect(win,self.color,(x,y,50,62),7)

def write_num(win):
	for i in range(9):
		for j in range(9):
			if aa.board1[i][j] != 0:
				font = pygame.font.SysFont(None, 30)
				img = font.render(str(aa.board[i][j]), True, (0,0,0))
				win.blit(img, (j*50+20,i*62+20 ))


pygame.init()


HEIGHT , WIDTH = 558,450

win  = pygame.display.set_mode((WIDTH,HEIGHT))
def draw_lines(win):
	global HEIGHT,WIDTH
	a = 0
	b = 0
	c = 2
	for i in range(9):
		if i %3==0:c = 3
		pygame.draw.line(win,(0,0,0),(a,0),(a,HEIGHT),c)
		a+=50
		pygame.draw.line(win,(0,0,0),(0,b),(WIDTH,b),c)
		b+=62
		c = 2
def write_text(win):
	pass

def draw_window(win):

	global m
	win.fill((255,255,255))
	draw_lines(win)
	if a: m.draw(win)
	write_num(win)
	pygame.display.update()

a = False
run = True
while run:
	text = ""

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			x , y = pygame.mouse.get_pos()
			x0 = x//50
			y0 = y//62
			a = True
			m= Cube([y0,x0])
		if event.type == pygame.KEYDOWN:
			text+=event.unicode
			m.value = int(text)
			if m.get_validation():m.color = (0,200,23)
			else : m.color = (222,12,21)



	draw_window(win)