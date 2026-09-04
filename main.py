import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)   
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Asteroid.containers = (asteroids, updatable, drawable)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
            

if __name__ == "__main__":
    main()
