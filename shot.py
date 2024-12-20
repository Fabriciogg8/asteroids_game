import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(surface=screen,color="green",center=self.position,radius=self.radius, width=1)
    
    def update(self, dt):
        self.position += (self.velocity * dt)