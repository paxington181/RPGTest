import pygame
from progconstants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)



def main():
    pygame.init
    pygame.display.set_caption("Character Sheet Tool")
    clock = pygame.time.Clock()
    
    dt = 0

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
    font = pygame.font.Font()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("dark blue")
        





        pygame.display.flip()
     
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()