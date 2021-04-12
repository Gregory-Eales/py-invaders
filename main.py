import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer


def load_sprites():
	sheet = pygame.image.load("assets/sprites.png").convert()

def main():

	mixer.init()
	mixer.music.load("assets/song.mp3")
	mixer.music.set_volume(0.7)
	mixer.music.play()

	BLACK = (0,0,0)
	(width, height) = (300, 200)


	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Py-Invaders')
	screen.fill(BLACK)
	pygame.display.flip()
	running = True


	while running:
	  for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	      running = False

if __name__ == "__main__":
	main()