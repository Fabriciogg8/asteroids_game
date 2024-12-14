import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass 
    
    def check_collisions(self, other_object):
            # Calculate the sum of the radii
            radius_sum = self.radius + other_object.radius
            # Check the distance between the two objects
            distance = self.position.distance_to(other_object.position)
            # Return True if the distance is less than or equal to the sum of the radii
            return distance <= radius_sum