import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position, new_velocity_1, new_radius)
        new_asteroid_2 = Asteroid(self.position, new_velocity_2, new_radius)

        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2.velocity = new_velocity_2 * 1.2

        for group in self.groups():
            group.add(new_asteroid_1)
            group.add(new_asteroid_2)

        self.kill()

