import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH



def main():
	pygame.init()	#inicializa pygame

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # establece las dimensiones de la pantalla
	
	clock = pygame.time.Clock() # establece el reloj
	dt = 0 #delta time entre cada frame dibujado
	
	running = True



	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill('orange')

		#Renderizar el juego aca

		pygame.display.flip()

		dt = clock.tick(60)/1000

pygame.quit()


if __name__ == '__main__':
	main()