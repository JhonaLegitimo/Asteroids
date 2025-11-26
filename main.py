from logger import log_state
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
playersito = Player(x, y)

VERSION = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        playersito.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick() / 1000
        log_state()


if __name__ == "__main__":
    main()
