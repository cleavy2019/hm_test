import random

import pygame

FONT_PX = 20

pygame.init()

winSur = pygame.display.set_mode((1280, 720))

font = pygame.font.SysFont("fangsong", 20)

bg_suface = pygame.Surface((1280, 720), flags=pygame.SRCALPHA)

pygame.Surface.convert(bg_suface)

bg_suface.fill(pygame.Color(1, 2, 4, 13))

winSur.fill((0, 0, 0))

# 相关参数
texts = [font.render(str(i), True, (100, 255, 100)) for i in range(3)]
colums = int(1280 / FONT_PX)
drops = [0 for i in range(colums)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(0)

    winSur.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))

        drops[i] += 1
        if drops[i] * 10 > 720 or random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()