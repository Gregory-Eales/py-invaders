import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer
from spritesheet import Spritesheet


def load_sprites():
	
	sprites = {}

	ss = Spritesheet('assets/large_sprites.png')

	sprites['player'] = ss.image_at((72, 32, 16, 8))
	sprites['boss'] = ss.image_at((72, 16, 16, 16))
	sprites['warning'] = ss.image_at((0, 96, 64, 8))
	sprites['top-bar'] = ss.image_at((0, 104, 128, 32))

	return sprites

def main():

	WIDTH = 640
	HEIGHT = 640
	VOLUME = 0.10
	BLACK = (0,0,0)
	CAPTION = 'Py-Invaders'

	PX = 0
	PY = 0

	PVX = 0
	PVY = 0


	# music
	mixer.init()
	mixer.music.load("assets/song.mp3")
	mixer.music.set_volume(VOLUME)
	mixer.music.play()

	# load screen
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(CAPTION)
	screen.fill(BLACK)
	pygame.display.flip()
	running = True
	clock = pygame.time.Clock()


	sprites = load_sprites()	
	img = sprites['player']

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
					PVY -= 10

				if event.key == pygame.K_DOWN:
					PVY += 10
			
			if PVX !=0:	
				PVX = PVX - PVX/abs(PVX)
			if PVY !=0:
				PVY = PVY - PVY/abs(PVY)  

		PX += PVX
		PY += PVY

		#if PX !=0 and PVX==0 and PVY==0:
			#PX =  PX - PX/abs(PX)

		#if PY !=0 and PVY==0 and PVX==0:
			#PY =  PY - PY/abs(PY) 

		screen.fill(BLACK)
		screen.blit(img, (PX,PY))
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()