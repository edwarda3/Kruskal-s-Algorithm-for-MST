from euclidianmst import findMST
import pygame
import time
import random

maxX = 50
maxY = 40
PPU = 20

def update(screen,font,graph,tree):
	screen.fill((220,220,220))
	for vertex in graph:
		(x,y) = vertex
		pos = (int(x*PPU),int(y*PPU))
		pygame.draw.circle(screen,(0,0,0),pos,3)
	for edge in tree:
		((x1,y1),(x2,y2)) = edge
		startpos = (int(x1*PPU),int(y1*PPU))
		endpos = (int(x2*PPU),int(y2*PPU))
		pygame.draw.aaline(screen,(150,0,0),startpos,endpos)

if __name__ == "__main__":
	graph = []
	(_,tree) = findMST(graph)

	pygame.init()
	pygame.font.init()
	myfont = pygame.font.SysFont('Ariel', 20)
	screen = pygame.display.set_mode((maxX*PPU,maxY*PPU))
	pygame.display.set_caption('LMouse: add point to cursor pos; RMouse: scatter 50 points')

	screen.fill((220,220,220))
	update(screen,myfont,graph,tree)

	mouseX ,mouseY = 0,0
	m1,m2,m3 = False,False,False
	m1r,m2r,m3r = True,True,True

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit() 
				sys.exit()
			if(event.type == pygame.KEYDOWN): 
				if(event.key == pygame.K_SPACE):
					graph = []
					tree = []
					update(screen,myfont,graph,tree)

		mouseX,mouseY = pygame.mouse.get_pos()
		m1,m2,m3 = pygame.mouse.get_pressed()
		
		if(m1 and m1r):
			graph.append((mouseX/PPU,mouseY/PPU))
			(_,tree) = findMST(graph)
			update(screen,myfont,graph,tree)
			m1r = False
		if(not m1 and not m1r):
			m1r = True
		if(m3 and m3r):
			for _ in range(50):
				graph.append((random.random()*maxX,random.random()*maxY))
			(_,tree) = findMST(graph)
			update(screen,myfont,graph,tree)
			m3r = False
		if(not m3 and not m3r):
			m3r = True

		pygame.display.update()