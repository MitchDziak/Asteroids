import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # must be done before any Player objects are created. This line puts all future Player objects in these two groups.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # allows x'ing out of the program
                return
            
        dt = (clock.tick(60)) / 1000  # limits framerate to 60FPS 

        updatable.update(dt)          # updates objects in classes in updatable Group. Currenly only player, will need to refactor when asteroids are added.
        screen.fill(color=(0, 0, 0))  # sets screen fill to black
        for entity in drawable:       # draws all objects from the classes in drawable Group
            entity.draw(screen)

        pygame.display.flip()





if __name__ == "__main__":
    main()
