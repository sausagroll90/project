import pygame
from math import sin, cos

pygame.init()

size = (1280, 700)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("scroller")

done = False

clock = pygame.time.Clock()

colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255)}

groundx = 0

char = pygame.image.load("char.png").convert_alpha()
charl = pygame.transform.flip(char, True, False)

chardirec = "right"

y_vel = 0.0

char_y = 490

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		groundxvel = 6
		chardirec = "left"
	elif keys[pygame.K_d] == True:
		groundxvel = -6
		chardirec = "right"
	else:
		groundxvel = 0
	
	groundx += groundxvel
	
	if keys[pygame.K_SPACE] == True and (groundcollide.colliderect(ground) or groundcollide.colliderect(ground2)):
		y_vel = 17.0
	
	char_y -= y_vel
	
	ground = pygame.Rect(0 + groundx, 640, 1280, 60)
	ground2 = pygame.Rect(1280 + groundx, 560, 1280, 60)
	groundcollide = pygame.Rect(639, (char_y + 150 - y_vel), 74, 1)
	
	if groundcollide.colliderect(ground):
		y_vel = 0.0
		char_y = ground.y - 150
	elif groundcollide.colliderect(ground2):
		y_vel = 0.0
		char_y = ground2.y - 150
	elif y_vel > -20:
		y_vel -= 1
	
	screen.fill(colours["cyan"])
	
	pygame.draw.rect(screen, colours["green"], ground, 0)
	pygame.draw.rect(screen, colours["green"], ground2, 0)
	#pygame.draw.rect(screen, colours["red"], groundcollide, 0)
	
	if chardirec == "right":
		screen.blit(char, (620, char_y))
	else:
		screen.blit(charl, (620, char_y))
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()