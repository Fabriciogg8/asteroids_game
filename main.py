# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame 
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player_init_x = SCREEN_WIDTH / 2
    player_init_y = SCREEN_HEIGHT / 2
    player = Player(player_init_x,player_init_y,PLAYER_RADIUS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) 
        dt = delta_time/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()