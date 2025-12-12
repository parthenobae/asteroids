import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,
                           LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        a = random.uniform(20, 50)
        b = self.velocity.rotate(a)
        c = self.velocity.rotate(-a)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid_b = Asteroid(self.position[0], self.position[1], new_radius)
        astroid_c = Asteroid(self.position[0], self.position[1], new_radius)
        astroid_b.velocity = b*1.2
        astroid_c.velocity = c*1.2
