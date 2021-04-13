import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer
from spritesheet import Spritesheet

#------------------------------#
WIDTH = 640
HEIGHT = 640
VOLUME = 1.00
BLACK = (0,0,0)
CAPTION = 'Py-Invaders'
#------------------------------#


def load_sprites():
	
	sprites = {}

	ss = Spritesheet('assets/large_sprites.png')

	sprites['player'] = ss.image_at((72, 32, 16, 8))
	sprites['boss'] = ss.image_at((72, 16, 16, 16))
	sprites['warning'] = ss.image_at((0, 96, 64, 8))
	sprites['top-bar'] = ss.image_at((0, 104, 128, 32))
	sprites['bullet'] = ss.image_at((16, 8, 8, 8))
	return sprites


def title_screen():

	# music
	mixer.init()
	mixer.music.load("assets/song.mp3")
	mixer.music.set_volume(VOLUME)
	mixer.music.play()


def main():

	
	# music
	mixer.init()
	mixer.music.load("assets/song.mp3")
	mixer.music.set_volume(VOLUME)
	

	laser_sound = pygame.mixer.Sound("assets/laser.wav")

	# load screen
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(CAPTION)
	screen.fill(BLACK)
	pygame.display.flip()
	running = True
	clock = pygame.time.Clock()

	bg = pygame.image.load('assets/background.png')

	title = pygame.image.load('assets/title.png')
	title_message = pygame.image.load('assets/title-message.png')
	title_message = pygame.transform.scale(
		title_message,
		(int(1097/4), int(74/4)),
	)

	sprites = load_sprites()	
	img = sprites['player']
	#img = img.convert_alpha(screen)

	mixer.music.play()
	#------------------------------------------------#
	counter = 0
	while running:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.KEYDOWN:
				running = False

		screen.fill(BLACK)

		screen.blit(bg, (0,0))
		screen.blit(title, (40,120))

		counter += 1
		if counter < 45:
			screen.blit(title_message, (185, 400))

		if counter >= 90:
			counter = 0
		
		pygame.display.flip()
		clock.tick(60)

	#------------------------------------------------#
	
	PX = 0
	PY = 560

	PVX = 0
	PVY = 0

	bullets = []

	running = True
	while running:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					PVX -= 10

				if event.key == pygame.K_RIGHT:
					PVX += 10

				if event.key == pygame.K_UP:
					#PVY -= 10
					pass

				if event.key == pygame.K_DOWN:
					#PVY += 10
					pass

				if event.key == pygame.K_SPACE:
					mixer.Sound.play(laser_sound)
					bullets.append([PX+20, PY-32])
			
			if PVX !=0:	
				PVX = PVX - PVX/abs(PVX)
			#if PVY !=0:
				#PVY = PVY - PVY/abs(PVY)  

		PX += PVX
		#PY += PVY

		#if PX !=0 and PVX==0 and PVY==0:
			#PX =  PX - PX/abs(PX)

		#if PY !=0 and PVY==0 and PVX==0:
			#PY =  PY - PY/abs(PY) 

		screen.fill(BLACK)
		#screen.blit(bg, (0,0))
		screen.blit(img, (PX,PY))

		for i in range(len(bullets)):
			bullets[i][1] -= 5
			screen.blit(
				sprites['bullet'],
				(bullets[i][0], bullets[i][1])
				)

		
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()