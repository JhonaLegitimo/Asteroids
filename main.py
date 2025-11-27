from logger import log_state
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")

VERSION = pygame.version.ver
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2


def main():
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable, asteroids)
    player= Player(x, y)

    print(f"Starting Asteroids with pygame version: {VERSION}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        dt = clock.tick() / 1000
        updatable.update(dt)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
