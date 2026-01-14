import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # allows x'ing out of the program
                return
            
        screen.fill(color=(0, 0, 0))  # sets screen fill to black
        pygame.display.flip()

        dt = (clock.tick(60)) / 1000  # limits framerate to 60FPS



if __name__ == "__main__":
    main()
