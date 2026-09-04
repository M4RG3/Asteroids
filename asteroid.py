import circleshape
import pygame
import constants
import random

from logger import log_event

class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH )

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        
    def split(self) -> None:
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return #bb asteroid
        
        log_event("asteroid_split")

        random_angle = random.uniform(20.0, 50.0)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        
        smaller_asteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        asteroid1.velocity = vector1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        asteroid2.velocity = vector2 * 1.2