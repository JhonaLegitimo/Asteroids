from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __intit__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid.velocity = self.velocity.rotate(angle)
        new_asteroid2.velocity = self.velocity.rotate(-angle)
        new_asteroid.velocity *= 1.2
        new_asteroid2.velocity *= 1.2
        return (new_asteroid, new_asteroid2)
            