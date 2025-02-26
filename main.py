import pygame
import pygame.freetype
from progconstants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)



def main():
    pygame.init
    pygame.display.set_caption("Character Sheet Tool")
    clock = pygame.time.Clock()
    font = pygame.freetype.Font("swansea-font/Swansea-q3pd.ttf", 30)
    dt = 0

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
    font = pygame.font.Font()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        screen.fill("dark blue")
        text_surface = font.render('Some Text', False, (0, 0, 0))
        screen.blit(text_surface, (40, 250))





        pygame.display.flip()
     
        dt = clock.tick(24) / 1000


if __name__ == "__main__":
    main()